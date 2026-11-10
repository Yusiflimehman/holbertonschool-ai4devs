// Simulated API call: resolves with a user object after a short delay
function fetchUser(id) {
  return new Promise((resolve) => {
    setTimeout(() => resolve({ id, name: `User${id}` }), 50);
  });
}

async function getUserNames(ids) {
  const users = await Promise.all(ids.map((id) => fetchUser(id)));
  return users.map((user) => user.name);
}

async function main() {
  const names = await getUserNames([1, 2, 3]);
  console.log(`Loaded ${names.length} users:`, names);
}

main();
