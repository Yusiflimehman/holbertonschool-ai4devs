import asyncio

async def fetch_user_data(user_id):
    await asyncio.sleep(1)
    return {"user_id": user_id, "status": "active"}

def process_users(user_ids):
    results = []
    for uid in user_ids:
        # Bug: Calling async function synchronously without await / event loop execution
        data = fetch_user_data(uid)
        results.append(data)
    return results

if __name__ == "__main__":
    users = [1, 2, 3]
    # Expected: list of dicts, Actual: list of un-awaited coroutine objects
    print(process_users(users))
