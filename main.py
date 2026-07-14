from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mock Guardrails API", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

security = HTTPBearer()
BEARER_TOKEN = "sk-mock-api-9f2a3c7e1b4d6f8a2c0e5g7i9k1m3o5q7s9u1w3y5"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing Bearer token")
    return credentials.credentials

@app.get("/api/v1/users")
def get_users(token: str = Depends(verify_token)):
    return {"users": [{"id": "usr_001","name": "Alice Johnson","email": "alice.johnson@acme-corp.com","phone": "+1 (212) 555-0147","ssn": "372-82-9156","role": "admin"},{"id": "usr_002","name": "Bob Martinez","email": "b.martinez@acme-corp.com","phone": "+1 (415) 555-0293","ssn": "519-47-3821","role": "analyst"},{"id": "usr_003","name": "Carol Smith","email": "carol.smith@acme-corp.com","phone": "+1 (650) 555-0061","ssn": "284-63-7014","role": "developer"}]}

@app.get("/api/v1/payments")
def get_payments(token: str = Depends(verify_token)):
    return {"payments": [{"id": "pay_001","user_id": "usr_001","card_number": "4532 1151 0823 9147","card_type": "Visa","expiry": "09/27","cvv": "412","cardholder": "Alice Johnson","amount": 1250.00,"status": "completed"},{"id": "pay_002","user_id": "usr_002","card_number": "5425 2334 3010 9903","card_type": "Mastercard","expiry": "03/26","cvv": "289","cardholder": "Bob Martinez","amount": 780.50,"status": "pending"}]}

@app.get("/api/v1/credentials/aws")
def get_aws_credentials(token: str = Depends(verify_token)):
    return {"aws_credentials": [{"id": "cred_aws_001","user_id": "usr_001","access_key_id": "AKIAIOSFODNN7EXAMPLE","secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY","region": "us-east-1","environment": "production"},{"id": "cred_aws_002","user_id": "usr_003","access_key_id": "AKIAI44QH8DHBEXAMPLE","secret_access_key": "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY","region": "eu-west-1","environment": "staging"}]}

@app.get("/api/v1/credentials/github")
def get_github_tokens(token: str = Depends(verify_token)):
    return {"github_tokens": [{"id": "cred_gh_001","user_id": "usr_001","token": "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","scopes": ["repo","read:org","workflow"],"created_at": "2024-11-01T09:00:00Z","expires_at": "2025-11-01T09:00:00Z"},{"id": "cred_gh_002","user_id": "usr_003","token": "github_pat_TEST1234567890_abcdefghijklmnopqrstuvwxyz","scopes": ["repo","admin:org"],"created_at": "2025-01-15T14:30:00Z","expires_at": "2026-01-15T14:30:00Z"}]}

@app.get("/api/v1/credentials/jwt")
def get_jwt_tokens(token: str = Depends(verify_token)):
    return {"jwt_tokens": [{"id": "jwt_001","user_id": "usr_002","token": "eyJraWQiOiJLMFpTOVFSZjcwSTlyUXdvNUwyZGJJUGxIV0RnZFhrWHd2N1g4dHVIMGJRPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJlNWU1ZDhlOS03ZmNlLTQ5N2EtOWU5Zi1mM2YzYWVkOTBkYzIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtd2VzdC0yLmFtYXpvbmF3cy5jb21cL2V1LXdlc3QtMl9UcGpGN2p4NTUiLCJjbGllbnRfaWQiOiI1NWdmMTlmcHJ0MXZlamhiMWd0MzhtaGw2MCIsIm9yaWdpbl9qdGkiOiJlZDc4NzI4Ny0zMWMwLTRkN2MtYTk4ZS0xNjc4ZWRhMGFhYzQiLCJldmVudF9pZCI6ImE0MjhkNzNkLTM2ZGItNDg1Zi1iMjY5LWY5ZDBkNTg2ZWVjNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3NjUxODgzNzEsImV4cCI6MTc2NTM2MjQ4MiwiaWF0IjoxNzY1MzU4ODgyLCJqdGkiOiIwMzI2NTE3NS1kOThlLTQ4MzUtYWY1MS0zMzlkYzI2MTRjODYiLCJ1c2VybmFtZSI6ImU1ZTVkOGU5LTdmY2UtNDk3YS05ZTlmLWYzZjNhZWQ5MGRjMiJ9.Hgzo0ul5SWZ32swSSJCcqr27QPh3wZ6uk7HZI4psVX3EP6OWGUNmm-rCMyKUobAv1ITuc92j49vJhH5Gxl4DTMNZDkAyTJik5r9niJ07uj5-CWWSW37WDNKGvfbzFCtJ0QJ76dEaVIff6z3tXskA9Hb-8-LmXi13Mymmgvp3_FV-IKW26Wi2GVLnqHjNAnmjHbg2_6SgeRBIq8aySlu_GzhKLpS3pDcox7KFQ1pQR4YPXnLk4VZ_BbznWr_6c4na2mEwudp2lk7F3umQW_7_n0Y5nXTnUgMiT2UBceUpUCcfyQTBGwoMZaf5PpChMaDA1VzeDngeKyHHyw9eM8LncQ"}]}

@app.get("/api/v1/credentials/api-keys")
def get_api_keys(token: str = Depends(verify_token)):
    return {
  "api_keys": [
    {
      "id": "apikey_001",
      "service": "Stripe",
      "key": "sk_live_51N8r8hKx9YzAbCdEfGhIjKlMnOpQrStUvWxYz0123456789ABCDEF",
      "environment": "production",
      "created_by": "usr_001"
    },
    {
      "id": "apikey_002",
      "service": "SendGrid",
      "key": "SG.xYzAbCdEfGhIjKlMnOpQrStUvWxYz0123456789ABCDEFghijklmnop",
      "environment": "production",
      "created_by": "usr_002"
    },
    {
      "id": "apikey_003",
      "service": "Twilio",
      "key": "SK4f8c2a9d7b6e5f1c3a2b9d8e7f6a5c4",
      "environment": "staging",
      "created_by": "usr_003"
    }
  ]
}

@app.get("/api/v1/all-sensitive")
def get_all_sensitive(token: str = Depends(verify_token)):
    return {"record": {"user": {"name": "Alice Johnson","email": "alice.johnson@acme-corp.com","phone": "+1 (212) 555-0147","ssn": "372-82-9156"},"payment": {"card_number": "4532 1151 0823 9147","cvv": "412"},"aws": {"access_key_id": "AKIAIOSFODNN7EXAMPLE","secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"},"github_token": "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","token": "eyJraWQiOiJLMFpTOVFSZjcwSTlyUXdvNUwyZGJJUGxIV0RnZFhrWHd2N1g4dHVIMGJRPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJlNWU1ZDhlOS03ZmNlLTQ5N2EtOWU5Zi1mM2YzYWVkOTBkYzIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtd2VzdC0yLmFtYXpvbmF3cy5jb21cL2V1LXdlc3QtMl9UcGpGN2p4NTUiLCJjbGllbnRfaWQiOiI1NWdmMTlmcHJ0MXZlamhiMWd0MzhtaGw2MCIsIm9yaWdpbl9qdGkiOiJlZDc4NzI4Ny0zMWMwLTRkN2MtYTk4ZS0xNjc4ZWRhMGFhYzQiLCJldmVudF9pZCI6ImE0MjhkNzNkLTM2ZGItNDg1Zi1iMjY5LWY5ZDBkNTg2ZWVjNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3NjUxODgzNzEsImV4cCI6MTc2NTM2MjQ4MiwiaWF0IjoxNzY1MzU4ODgyLCJqdGkiOiIwMzI2NTE3NS1kOThlLTQ4MzUtYWY1MS0zMzlkYzI2MTRjODYiLCJ1c2VybmFtZSI6ImU1ZTVkOGU5LTdmY2UtNDk3YS05ZTlmLWYzZjNhZWQ5MGRjMiJ9.Hgzo0ul5SWZ32swSSJCcqr27QPh3wZ6uk7HZI4psVX3EP6OWGUNmm-rCMyKUobAv1ITuc92j49vJhH5Gxl4DTMNZDkAyTJik5r9niJ07uj5-CWWSW37WDNKGvfbzFCtJ0QJ76dEaVIff6z3tXskA9Hb-8-LmXi13Mymmgvp3_FV-IKW26Wi2GVLnqHjNAnmjHbg2_6SgeRBIq8aySlu_GzhKLpS3pDcox7KFQ1pQR4YPXnLk4VZ_BbznWr_6c4na2mEwudp2lk7F3umQW_7_n0Y5nXTnUgMiT2UBceUpUCcfyQTBGwoMZaf5PpChMaDA1VzeDngeKyHHyw9eM8LncQ","api_key": "STRIPE_TEST_KEY_PLACEHOLDER_002"}}


# ---------------------------------------------------------------------------
# Write Idempotency (Retry Safety) test support
#
# Adds a flaky endpoint (GET + POST + PUT + DELETE) that returns 503 on the
# first request for a given path and 200 on every request after that, plus
# /reset and /counts so tests can drive and verify request counts
# deterministically. Reuses the same verify_token dependency as the rest of
# this API.
# ---------------------------------------------------------------------------

_flaky_counts: dict[str, int] = {}

def _flaky_response(path_key: str):
    _flaky_counts[path_key] = _flaky_counts.get(path_key, 0) + 1
    n = _flaky_counts[path_key]
    if n == 1:
        raise HTTPException(status_code=503, detail="Service Unavailable")
    return {"ok": True, "attempt": n}

@app.get("/api/v1/flaky")
def flaky_get(token: str = Depends(verify_token)):
    return _flaky_response("get")

@app.post("/api/v1/flaky")
def flaky_post(token: str = Depends(verify_token)):
    return _flaky_response("post")

@app.put("/api/v1/flaky")
def flaky_put(token: str = Depends(verify_token)):
    return _flaky_response("put")

@app.delete("/api/v1/flaky")
def flaky_delete(token: str = Depends(verify_token)):
    return _flaky_response("delete")

@app.post("/api/v1/flaky/reset")
def flaky_reset(token: str = Depends(verify_token)):
    _flaky_counts.clear()
    return {"reset": True}

@app.get("/api/v1/flaky/counts")
def flaky_counts(token: str = Depends(verify_token)):
    return dict(_flaky_counts)


# ---------------------------------------------------------------------------
# GraphQL mutation test support
#
# REST idempotency is inferred from the HTTP verb (GET/PUT/DELETE = safe to
# retry, POST = not). GraphQL has no such transport-level signal -- every
# operation goes over POST. Idempotency there is annotation-driven instead:
# the schema itself declares an operation as `Query` (read-only) or
# `Mutation` (a write, never safe to blindly retry), and a well-behaved
# client/executor must honor that schema-level annotation rather than
# guessing from the HTTP method.
#
# `flakyMutation` behaves like the REST flaky endpoints (503 on first call,
# success after) but is declared as a GraphQL Mutation, so a retry engine
# that respects the annotation should NOT retry it on transient failure.
# ---------------------------------------------------------------------------

import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info


_graphql_mutation_counts: dict[str, int] = {}


@strawberry.type
class MutationResult:
    ok: bool
    attempt: int


@strawberry.type
class Query:
    @strawberry.field(description="Read-only health check. Safe to retry.")
    def ping(self) -> str:
        return "pong"

    @strawberry.field(description="Read-only. Returns how many times flakyMutation has been called.")
    def flaky_mutation_count(self) -> int:
        return _graphql_mutation_counts.get("graphql_mutation", 0)


def _require_token(info: Info) -> None:
    request = info.context["request"]
    auth = request.headers.get("authorization", "")
    if not auth.startswith("Bearer ") or auth.removeprefix("Bearer ") != BEARER_TOKEN:
        raise Exception("Invalid or missing Bearer token")


@strawberry.type
class Mutation:
    @strawberry.mutation(
        description=(
            "Write operation (GraphQL Mutation, not Query). Non-idempotent and "
            "not retry-safe: repeating it can duplicate the write. Returns a "
            "transient failure on the first call, then succeeds -- a correct "
            "retry engine must NOT auto-retry this on error, since safety here "
            "is annotation-driven (Mutation type) rather than inferred from an "
            "HTTP verb."
        )
    )
    def flaky_mutation(self, info: Info) -> MutationResult:
        _require_token(info)
        key = "graphql_mutation"
        _graphql_mutation_counts[key] = _graphql_mutation_counts.get(key, 0) + 1
        n = _graphql_mutation_counts[key]
        if n == 1:
            raise Exception("Service Unavailable (transient)")
        return MutationResult(ok=True, attempt=n)

    @strawberry.mutation(description="Resets the GraphQL flaky mutation counter.")
    def reset_flaky_mutation(self, info: Info) -> bool:
        _require_token(info)
        _graphql_mutation_counts.clear()
        return True
# Add to main.py to support the "read-only query vs transient failure ->
# retried" test. Mirrors the existing flaky_mutation resolver, but as a
# Query field, so it's exercised as an idempotent read rather than a write.
#
# Placement: inside the `Query` class (alongside `ping` / `flaky_mutation_count`),
# and needs a counter dict + reset mutation alongside the existing
# `_graphql_mutation_counts` / `reset_flaky_mutation`.

_graphql_query_counts: dict[str, int] = {}

# --- inside class Query: ---
@strawberry.field(
    description=(
        "Read-only. Transient failure on first call, succeeds after. "
        "Idempotent -- safe for a retry engine to retry on transient error."
    )
)
def flaky_query(self) -> MutationResult:
    key = "graphql_query"
    _graphql_query_counts[key] = _graphql_query_counts.get(key, 0) + 1
    n = _graphql_query_counts[key]
    if n == 1:
        raise Exception("Service Unavailable (transient)")
    return MutationResult(ok=True, attempt=n)

# --- inside class Mutation: ---
@strawberry.mutation(description="Resets the GraphQL flaky query counter.")
def reset_flaky_query(self, info: Info) -> bool:
    _require_token(info)
    _graphql_query_counts.clear()
    return True

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, path="")
app.include_router(graphql_app, prefix="/api/v1/graphql")
