(*
    Portfolio excerpt: consume a sequence-numbered global plan from Python.
    Simplified from the reviewed TwinCAT implementation.
*)

NewPlanAccepted := FALSE;

IF IncomingPlan.seq_id <> 0
   AND IncomingPlan.seq_id <> LastAcceptedSeqId THEN

    ActivePlan.seq_id := IncomingPlan.seq_id;
    ActivePlan.timestamp_s := IncomingPlan.timestamp_s;

    FOR mover := 1 TO MAX_MOVERS DO
        ActivePlan.movers[mover].valid := IncomingPlan.movers[mover].valid;
        ActivePlan.movers[mover].id := IncomingPlan.movers[mover].id;

        nPoints := IncomingPlan.movers[mover].num_points;
        IF nPoints > MAX_WAYPOINTS THEN
            nPoints := MAX_WAYPOINTS;
        END_IF;

        ActivePlan.movers[mover].num_points := nPoints;

        IF ActivePlan.movers[mover].valid THEN
            FOR point := 1 TO nPoints DO
                ActivePlan.movers[mover].waypoints[point] :=
                    IncomingPlan.movers[mover].waypoints[point];
            END_FOR;
        END_IF;
    END_FOR;

    LastAcceptedSeqId := IncomingPlan.seq_id;
    AcceptedSeqId := IncomingPlan.seq_id;
    NewPlanAccepted := TRUE;   (* one-cycle acknowledgement pulse *)
END_IF;
