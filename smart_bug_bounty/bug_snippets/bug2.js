// Simulated API call: resolves with a user object after a short delay
function fetchUser(id) {
  return new Promise((resolve) => {
    setTimeout(() => resolve({ id, name: `User${id}` }), 50);
  });
}

async function getUserNames(ids) {
  const names = [];

  ids.forEach(async (id) => {
    const user = await fetchUser(id);
    names.push(user.name);
  });

  return names;
}

async function main() {
  const names = await getUserNames([1, 2, 3]);
  console.log(`Loaded ${names.length} users:`, names);
}

main();
