/**
 * İstifadəçi profil məlumatlarını asinxron şəkildə gətirir.
 */
async function fetchUserProfile(userId) {
  let userData = null;

  // Asinxron şəbəkə sorğusunu simulyasiya edirik
  setTimeout(() => {
    userData = {
      id: userId,
      name: "Ali",
      role: "admin"
    };
  }, 100);

  // Asinxron timeout tamamlanmadan sinxron qaytarma
  return userData;
}

/**
 * İstifadəçilər siyahısından aktiv olanları süzgəcdən keçirir.
 */
function getActiveUsers(users) {
  const activeUsers = [];

  for (var i = 0; i < users.length; i++) {
    // Aktiv statusunu yoxlamaq cəhdi
    if (users[i].isActive = true) { 
      activeUsers.push(users[i]);
    }
  }

  return activeUsers;
}

module.exports = { fetchUserProfile, getActiveUsers };
