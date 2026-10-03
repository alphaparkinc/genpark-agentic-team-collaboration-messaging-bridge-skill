"""Example usage for Agentic Team Collaboration Messaging Bridge."""
from client import TeamCollaborationMessagingBridge

if __name__ == "__main__":
    event = {
        "agent_id": "security-sentinel-v2",
        "event_type": "critical_error",
        "payload": {"reason": "Unauthorized access attempt blocked on port 8080"},
        "session_id": "session-sec-404"
    }
    routed = TeamCollaborationMessagingBridge.route_agent_message(event)
    print("Target Channel:", routed["target_channel"])
    print("Action Required:", routed["dispatch_card"]["requires_action"])
