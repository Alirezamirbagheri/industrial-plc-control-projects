(*
    Portfolio excerpt: local motion override takes priority over global motion.
    Simplified from the reviewed TwinCAT implementation.
*)

FOR slot := 1 TO MAX_MOVERS DO

    IF LocalOverride[slot].active THEN
        (* Local correction is executed first. Global progression is held for this mover. *)
        GlobalExec[slot].hold := TRUE;

        CASE LocalOverride[slot].step_state OF
            0:
                TargetPosition[slot] :=
                    CurrentPosition[slot] + LocalOverride[slot].target_delta;
                LocalOverride[slot].step_state := 1;

            1:
                IssueMoveCommand(slot, TargetPosition[slot]);
                LocalOverride[slot].step_state := 2;

            2:
                IF MoveDone(slot) THEN
                    LocalOverrideDoneByMover[slot] := TRUE;
                    LocalOverrideDoneSeqIdByMover[slot] :=
                        LocalOverride[slot].seq_id;

                    LocalOverride[slot].active := FALSE;
                    LocalOverride[slot].step_state := 0;
                    GlobalExec[slot].hold := FALSE;
                END_IF;
        END_CASE;

    ELSE
        (* No local correction is pending: continue the global waypoint plan. *)
        ExecuteGlobalWaypoint(slot);
    END_IF;

END_FOR;
