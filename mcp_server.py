"""MCP server for Agentic Team Collaboration Messaging Bridge."""
import sys
import json
from client import TeamCollaborationMessagingBridge

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "route_agent_event",
                "description": "Routes agent events to appropriate team workspace channels",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "incoming_event": {"type": "object"}
                    },
                    "required": ["incoming_event"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "route_agent_event":
            event = params.get("arguments", {}).get("incoming_event", {})
            res = TeamCollaborationMessagingBridge.route_agent_message(event)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
