const dataService = require('./dataService');

// Clear and initialize data before each test
beforeEach(() => {
  dataService.clearAllData();
});

// after each test, clear session or other cleanup
afterEach(() => {
  dataService.logout();
});
