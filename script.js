// Data service for managing pickup requests and feedback
// Uses localStorage for data persistence

const STORAGE_KEYS = {
  PICKUP_REQUESTS: 'cleancity_pickup_requests',
  FEEDBACK: 'cleancity_feedback',
  USERS: 'cleancity_users'
};

// Initialize with sample data if no data exists
const initializeData = () => {
  if (!localStorage.getItem(STORAGE_KEYS.PICKUP_REQUESTS)) {
    const sampleRequests = [
      {
        id: 'REQ001',
        name: 'John Doe',
        location: 'Nairobi',
        wasteType: 'General Waste',
        preferredDate: '2024-01-15',
        status: 'Pending'
      },
      {
        id: 'REQ002',
        name: 'Jane Smith',
        location: 'Kisumu',
        wasteType: 'Recyclable',
        preferredDate: '2024-01-16',
        status: 'Scheduled'
      },
      {
        id: 'REQ003',
        name: 'Mike Johnson',
        location: 'Mombasa',
        wasteType: 'Hazardous',
        preferredDate: '2024-01-17',
        status: 'Completed'
      },
      {
        id: 'REQ004',
        name: 'Sarah Wilson',
        location: 'Eldoret',
        wasteType: 'General Waste',
        preferredDate: '2024-01-18',
        status: 'Pending'
      },
      {
        id: 'REQ005',
        name: 'David Brown',
        location: 'Nairobi',
        wasteType: 'Recyclable',
        preferredDate: '2024-01-19',
        status: 'Missed'
      }
    ];
    localStorage.setItem(STORAGE_KEYS.PICKUP_REQUESTS, JSON.stringify(sampleRequests));
  }

  if (!localStorage.getItem(STORAGE_KEYS.FEEDBACK)) {
    localStorage.setItem(STORAGE_KEYS.FEEDBACK, JSON.stringify([]));
  }

  if (!localStorage.getItem(STORAGE_KEYS.USERS)) {
    const sampleUsers = [
      {
        id: '1',
        name: 'Demo User',
        email: 'user@cleancity.com',
        password: 'password123', // Plain text password (vulnerable)
        role: 'user',
        createdAt: '2024-01-01T00:00:00.000Z'
      },
      {
        id: '2',
        name: 'Admin User',
        email: 'admin@cleancity.com',
        password: 'admin123', // Plain text password (vulnerable)
        role: 'admin',
        createdAt: '2024-01-01T00:00:00.000Z'
      }
    ];
    localStorage.setItem(STORAGE_KEYS.USERS, JSON.stringify(sampleUsers));
  }
};

// Initialize data on module load
initializeData();

const dataService = {
  // Get all pickup requests
  getAllPickupRequests: () => {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.PICKUP_REQUESTS);
      return data ? JSON.parse(data) : [];
    } catch (error) {
      console.error('Error loading pickup requests:', error);
      return [];
    }
  },

  // Add a new pickup request
  addPickupRequest: (requestData) => {
    try {
      const requests = dataService.getAllPickupRequests();
      const newRequest = {
        id: `REQ${String(requests.length + 1).padStart(3, '0')}`,
        name: requestData.fullName,
        location: requestData.location,
        wasteType: requestData.wasteType,
        preferredDate: requestData.preferredDate || 'Not specified',
        status: 'Pending'
      };
      
      requests.push(newRequest);
      localStorage.setItem(STORAGE_KEYS.PICKUP_REQUESTS, JSON.stringify(requests));
      return newRequest;
    } catch (error) {
      console.error('Error adding pickup request:', error);
      return null;
    }
  },

  // Update request status
  updateRequestStatus: (requestId, newStatus) => {
    try {
      const requests = dataService.getAllPickupRequests();
      const requestIndex = requests.findIndex(req => req.id === requestId);
      
      if (requestIndex !== -1) {
        requests[requestIndex].status = newStatus;
        localStorage.setItem(STORAGE_KEYS.PICKUP_REQUESTS, JSON.stringify(requests));
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error updating request status:', error);
      return false;
    }
  },

  // Filter requests by status
  filterRequestsByStatus: (status) => {
    const requests = dataService.getAllPickupRequests();
    return requests.filter(request => request.status === status);
  },

  // Filter requests by location (subtle bug: Eldoret filter shows Nairobi data)
  filterRequestsByLocation: (location) => {
    const requests = dataService.getAllPickupRequests();
    if (location === 'Eldoret') {
      // Bug: Returns Nairobi requests instead of Eldoret
      return requests.filter(request => request.location === 'Nairobi');
    }
    return requests.filter(request => request.location === location);
  },

  // Get all feedback
  getAllFeedback: () => {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.FEEDBACK);
      return data ? JSON.parse(data) : [];
    } catch (error) {
      console.error('Error loading feedback:', error);
      return [];
    }
  },

  // Add new feedback
  addFeedback: (feedbackData) => {
    try {
      const feedback = dataService.getAllFeedback();
      const newFeedback = {
        id: Date.now(),
        requestId: feedbackData.requestId,
        reason: feedbackData.reason,
        comments: feedbackData.comments,
        timestamp: new Date().toISOString()
      };
      
      feedback.push(newFeedback);
      localStorage.setItem(STORAGE_KEYS.FEEDBACK, JSON.stringify(feedback));
      return newFeedback;
    } catch (error) {
      console.error('Error adding feedback:', error);
      return null;
    }
  },

  // User management functions (vulnerable to security attacks)
  getAllUsers: () => {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.USERS);
      return data ? JSON.parse(data) : [];
    } catch (error) {
      console.error('Error loading users:', error);
      return [];
    }
  },

  // Add new user (vulnerable - stores plain text passwords)
  addUser: (userData) => {
    try {
      const users = dataService.getAllUsers();
      
      // Check if user already exists
      const existingUser = users.find(u => u.email === userData.email);
      if (existingUser) {
        return false;
      }
      
      users.push(userData);
      localStorage.setItem(STORAGE_KEYS.USERS, JSON.stringify(users));
      return true;
    } catch (error) {
      console.error('Error adding user:', error);
      return false;
    }
  },

  // Get user by ID (vulnerable to IDOR attacks)
  getUserById: (userId) => {
    try {
      const users = dataService.getAllUsers();
      return users.find(u => u.id === userId);
    } catch (error) {
      console.error('Error getting user:', error);
      return null;
    }
  },

  // Get user by email (vulnerable to enumeration attacks)
  getUserByEmail: (email) => {
    try {
      const users = dataService.getAllUsers();
      return users.find(u => u.email === email);
    } catch (error) {
      console.error('Error getting user by email:', error);
      return null;
    }
  },

  // Update user (vulnerable - no authorization checks)
  updateUser: (userId, userData) => {
    try {
      const users = dataService.getAllUsers();
      const userIndex = users.findIndex(u => u.id === userId);
      
      if (userIndex !== -1) {
        users[userIndex] = { ...users[userIndex], ...userData };
        localStorage.setItem(STORAGE_KEYS.USERS, JSON.stringify(users));
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error updating user:', error);
      return false;
    }
  },

  // Delete user (vulnerable - no authorization checks)
  deleteUser: (userId) => {
    try {
      const users = dataService.getAllUsers();
      const filteredUsers = users.filter(u => u.id !== userId);
      
      if (filteredUsers.length < users.length) {
        localStorage.setItem(STORAGE_KEYS.USERS, JSON.stringify(filteredUsers));
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error deleting user:', error);
      return false;
    }
  },

  // Get current user from session
  getCurrentUser: () => {
    try {
      const userData = localStorage.getItem('currentUser');
      return userData ? JSON.parse(userData) : null;
    } catch (error) {
      console.error('Error getting current user:', error);
      return null;
    }
  },

  // Logout user
  logout: () => {
    try {
      localStorage.removeItem('currentUser');
      return true;
    } catch (error) {
      console.error('Error logging out:', error);
      return false;
    }
  },

  // Check if user is authenticated
  isAuthenticated: () => {
    return dataService.getCurrentUser() !== null;
  },

  // Check if user has admin role
  isAdmin: () => {
    const user = dataService.getCurrentUser();
    return user && user.role === 'admin';
  },

  // Clear all data (for testing)
  clearAllData: () => {
    localStorage.removeItem(STORAGE_KEYS.PICKUP_REQUESTS);
    localStorage.removeItem(STORAGE_KEYS.FEEDBACK);
    localStorage.removeItem(STORAGE_KEYS.USERS);
    localStorage.removeItem('currentUser');
    initializeData();
  }
};

// Application state
let currentUser = null;
let currentPage = 'home';

// Navigation functionality
function initNavigation() {
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetPage = link.getAttribute('data-page');
      
      if (targetPage) {
        navigateToPage(targetPage);
      }
    });
  });

  // Logout button
  const logoutBtn = document.getElementById('logout-btn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', (e) => {
      e.preventDefault();
      logout();
    });
  }

  // Hamburger menu
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('nav-menu');
  
  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });
  }
}

function navigateToPage(page) {
  // Hide all pages
  document.querySelectorAll('.page').forEach(p => p.style.display = 'none');
  
  // Show target page
  const targetPage = document.getElementById(`${page}-page`);
  if (targetPage) {
    targetPage.style.display = 'block';
    currentPage = page;
  }
  
  // Update navigation
  updateNavigation();
  
  // Load page-specific data
  loadPageData(page);
}

function updateNavigation() {
  const authLinks = document.getElementById('auth-links');
  const userLinks = document.getElementById('user-links');
  const adminLink = document.getElementById('admin-link');
  
  if (currentUser) {
    // User is logged in
    if (authLinks) authLinks.style.display = 'none';
    if (userLinks) userLinks.style.display = 'block';
    
    // Show admin link if user is admin
    if (adminLink) {
      adminLink.style.display = currentUser.role === 'admin' ? 'block' : 'none';
    }
    
    // Update user info
    updateUserInfo();
  } else {
    // User is not logged in
    if (authLinks) authLinks.style.display = 'block';
    if (userLinks) userLinks.style.display = 'none';
    if (adminLink) adminLink.style.display = 'none';
    
    // Hide user info
    const userInfo = document.getElementById('user-info');
    if (userInfo) userInfo.style.display = 'none';
  }
}

function updateUserInfo() {
  const userInfo = document.getElementById('user-info');
  const welcomeText = document.getElementById('welcome-text');
  const adminBadge = document.getElementById('admin-badge');
  
  if (userInfo && currentUser) {
    userInfo.style.display = 'flex';
    if (welcomeText) welcomeText.textContent = `Welcome, ${currentUser.name}`;
    if (adminBadge) {
      adminBadge.style.display = currentUser.role === 'admin' ? 'block' : 'none';
    }
  }
}

// Load page-specific data
function loadPageData(page) {
  switch(page) {
    case 'dashboard':
      if (currentUser) {
        loadDashboardData();
      } else {
        navigateToPage('login');
      }
      break;
    case 'feedback':
      if (currentUser) {
        loadFeedbackData();
      } else {
        navigateToPage('login');
      }
      break;
    case 'admin':
      if (currentUser && currentUser.role === 'admin') {
        loadAdminData();
      } else {
        navigateToPage('login');
      }
      break;
  }
}

// Authentication functions
function login(email, password) {
  // Simple authentication (vulnerable to various attacks)
  const users = dataService.getAllUsers();
  const user = users.find(u => 
    u.email === email && 
    u.password === password // Plain text password comparison
  );
  
  if (user) {
    // Store user session (vulnerable - no proper session management)
    const sessionUser = {
      id: user.id,
      email: user.email,
      name: user.name,
      role: user.role
    };
    
    localStorage.setItem('currentUser', JSON.stringify(sessionUser));
    currentUser = sessionUser;
    
    showMessage('login-success', 'Login successful! Redirecting...');
    setTimeout(() => {
      navigateToPage('dashboard');
    }, 1000);
    
    return true;
  } else {
    showMessage('login-error', 'Invalid email or password');
    return false;
  }
}

function register(userData) {
  // Check if user already exists
  const users = dataService.getAllUsers();
  const existingUser = users.find(u => u.email === userData.email);
  
  if (existingUser) {
    showMessage('register-error', 'User with this email already exists');
    return false;
  }
  
  // Create new user (vulnerable - stores plain text passwords)
  const newUser = {
    id: Date.now().toString(),
    name: userData.name,
    email: userData.email,
    password: userData.password, // Stored in plain text
    role: 'user',
    createdAt: new Date().toISOString()
  };
  
  const success = dataService.addUser(newUser);
  
  if (success) {
    showMessage('register-success', 'Registration successful! You can now login.');
    return true;
  } else {
    showMessage('register-error', 'Registration failed. Please try again.');
    return false;
  }
}

function logout() {
  dataService.logout();
  currentUser = null;
  navigateToPage('home');
}

// Form handling
function initForms() {
  // Login form
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', handleLoginSubmit);
  }
  
  // Register form
  const registerForm = document.getElementById('register-form');
  if (registerForm) {
    registerForm.addEventListener('submit', handleRegisterSubmit);
  }
  
  // Pickup form
  const pickupForm = document.getElementById('pickup-form');
  if (pickupForm) {
    pickupForm.addEventListener('submit', handlePickupSubmit);
  }
  
  // Feedback form
  const feedbackForm = document.getElementById('feedback-form');
  if (feedbackForm) {
    feedbackForm.addEventListener('submit', handleFeedbackSubmit);
  }
}

function handleLoginSubmit(e) {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const email = formData.get('email');
  const password = formData.get('password');
  
  login(email, password);
}

function handleRegisterSubmit(e) {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const userData = {
    name: formData.get('name'),
    email: formData.get('email'),
    password: formData.get('password'),
    confirmPassword: formData.get('confirmPassword')
  };
  
  // Basic validation
  if (!userData.name.trim()) {
    showMessage('register-error', 'Name is required');
    return;
  }
  
  if (!userData.email.trim()) {
    showMessage('register-error', 'Email is required');
    return;
  }
  
  // Weak email validation
  if (!userData.email.includes('@')) {
    showMessage('register-error', 'Please enter a valid email address');
    return;
  }
  
  if (!userData.password) {
    showMessage('register-error', 'Password is required');
    return;
  }
  
  // Weak password validation (vulnerable)
  if (userData.password.length < 3) {
    showMessage('register-error', 'Password must be at least 3 characters long');
    return;
  }
  
  if (userData.password !== userData.confirmPassword) {
    showMessage('register-error', 'Passwords do not match');
    return;
  }
  
  const success = register(userData);
  if (success) {
    e.target.reset();
  }
}

function handlePickupSubmit(e) {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const data = {
    fullName: formData.get('fullName'),
    location: formData.get('location'),
    wasteType: formData.get('wasteType'),
    preferredDate: formData.get('preferredDate')
  };
  
  const errors = validatePickupForm(data);
  
  if (Object.keys(errors).length === 0) {
    const newRequest = dataService.addPickupRequest(data);
    if (newRequest) {
      showMessage('success-message', 'Request submitted successfully!');
      e.target.reset();
    } else {
      alert('Failed to submit request. Please try again.');
    }
  } else {
    displayPickupErrors(errors);
  }
}

function validatePickupForm(data) {
  const errors = {};
  
  // Validate full name (subtle flaw: allows very short names)
  if (!data.fullName.trim()) {
    errors.fullName = 'Full name is required';
  } else if (data.fullName.trim().length < 2) {
    // Subtle flaw: should be at least 3 characters but allows 2
    errors.fullName = 'Name must be at least 2 characters';
  }
  
  // Validate location
  if (!data.location) {
    errors.location = 'Please select a location';
  }
  
  // Validate waste type
  if (!data.wasteType) {
    errors.wasteType = 'Please select a waste type';
  }
  
  // Subtle flaw: Missing validation for preferred date
  // The field appears optional but should be required for scheduling
  
  return errors;
}

function displayPickupErrors(errors) {
  // Clear previous errors
  document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
  
  // Display new errors
  if (errors.fullName) {
    document.getElementById('name-error').textContent = errors.fullName;
  }
  if (errors.location) {
    document.getElementById('location-error').textContent = errors.location;
  }
  if (errors.wasteType) {
    document.getElementById('waste-error').textContent = errors.wasteType;
  }
}

function handleFeedbackSubmit(e) {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const data = {
    requestId: formData.get('requestId'),
    reason: formData.get('reason'),
    comments: formData.get('comments')
  };
  
  const errors = validateFeedbackForm(data);
  
  if (Object.keys(errors).length === 0) {
    const newFeedback = dataService.addFeedback(data);
    if (newFeedback) {
      showMessage('feedback-success', 'Feedback submitted successfully!');
      e.target.reset();
    } else {
      alert('Failed to submit feedback. Please try again.');
    }
  } else {
    displayFeedbackErrors(errors);
  }
}

function validateFeedbackForm(data) {
  const errors = {};
  
  // Basic validation for Request ID
  if (!data.requestId.trim()) {
    errors.requestId = 'Request ID is required';
  }
  
  // Validate reason
  if (!data.reason) {
    errors.reason = 'Please select a reason';
  }
  
  // Subtle flaw: No validation for comments
  // Should require comments for proper feedback tracking
  
  return errors;
}

function displayFeedbackErrors(errors) {
  // Clear previous errors
  document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
  
  // Display new errors
  if (errors.requestId) {
    document.getElementById('requestId-error').textContent = errors.requestId;
  }
  if (errors.reason) {
    document.getElementById('reason-error').textContent = errors.reason;
  }
}

// Dashboard functionality
function loadDashboardData() {
  const requests = dataService.getAllPickupRequests();
  displayRequests(requests, 'requests-tbody');
  updateFilterCount(requests.length, requests.length);
  
  // Setup filters
  setupDashboardFilters();
}

function setupDashboardFilters() {
  const statusFilter = document.getElementById('statusFilter');
  const locationFilter = document.getElementById('locationFilter');
  
  if (statusFilter) {
    statusFilter.addEventListener('change', applyFilters);
  }
  if (locationFilter) {
    locationFilter.addEventListener('change', applyFilters);
  }
}

function applyFilters() {
  const statusFilter = document.getElementById('statusFilter');
  const locationFilter = document.getElementById('locationFilter');
  
  let filteredRequests = dataService.getAllPickupRequests();
  
  // Apply status filter
  if (statusFilter && statusFilter.value !== 'all') {
    filteredRequests = dataService.filterRequestsByStatus(statusFilter.value);
  }
  
  // Apply location filter
  if (locationFilter && locationFilter.value !== 'all') {
    filteredRequests = dataService.filterRequestsByLocation(locationFilter.value);
  }
  
  displayRequests(filteredRequests, 'requests-tbody');
  updateFilterCount(filteredRequests.length, dataService.getAllPickupRequests().length);
}

function displayRequests(requests, tbodyId) {
  const tbody = document.getElementById(tbodyId);
  if (!tbody) return;
  
  tbody.innerHTML = '';
  
  requests.forEach(request => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${request.id}</td>
      <td>${request.name}</td>
      <td>${request.location}</td>
      <td>${request.wasteType}</td>
      <td>${request.preferredDate}</td>
      <td><span class="status-badge status-${request.status.toLowerCase()}">${request.status}</span></td>
    `;
    tbody.appendChild(row);
  });
}

function updateFilterCount(filtered, total) {
  const filterCount = document.getElementById('filter-count');
  if (filterCount) {
    filterCount.textContent = `Showing ${filtered} of ${total} requests`;
  }
}

// Admin functionality
function loadAdminData() {
  const requests = dataService.getAllPickupRequests();
  displayAdminRequests(requests);
  updateStatistics(requests);
  setupAdminControls(requests);
}

function displayAdminRequests(requests) {
  const tbody = document.getElementById('admin-tbody');
  if (!tbody) return;
  
  tbody.innerHTML = '';
  
  requests.forEach(request => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${request.id}</td>
      <td>${request.name}</td>
      <td>${request.location}</td>
      <td>${request.wasteType}</td>
      <td>${request.preferredDate}</td>
      <td><span class="status-badge status-${request.status.toLowerCase()}">${request.status}</span></td>
      <td>
        <button class="btn btn-sm btn-outline-primary edit-btn" data-id="${request.id}">
          Edit
        </button>
      </td>
    `;
    tbody.appendChild(row);
  });
  
  // Add event listeners to edit buttons
  document.querySelectorAll('.edit-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const requestId = e.target.getAttribute('data-id');
      const request = requests.find(r => r.id === requestId);
      if (request) {
        const requestSelect = document.getElementById('requestSelect');
        const statusSelect = document.getElementById('statusSelect');
        const updateBtn = document.getElementById('updateStatusBtn');
        
        if (requestSelect) requestSelect.value = requestId;
        if (statusSelect) statusSelect.value = '';
        if (updateBtn) updateBtn.disabled = false;
      }
    });
  });
}

function updateStatistics(requests) {
  const totalRequests = document.getElementById('totalRequests');
  const pendingRequests = document.getElementById('pendingRequests');
  const scheduledRequests = document.getElementById('scheduledRequests');
  const completedRequests = document.getElementById('completedRequests');
  
  if (totalRequests) totalRequests.textContent = requests.length;
  if (pendingRequests) pendingRequests.textContent = requests.filter(r => r.status === 'Pending').length;
  if (scheduledRequests) scheduledRequests.textContent = requests.filter(r => r.status === 'Scheduled').length;
  if (completedRequests) completedRequests.textContent = requests.filter(r => r.status === 'Completed').length;
}

function setupAdminControls(requests) {
  const requestSelect = document.getElementById('requestSelect');
  const statusSelect = document.getElementById('statusSelect');
  const updateBtn = document.getElementById('updateStatusBtn');
  
  if (requestSelect) {
    // Populate request select
    requestSelect.innerHTML = '<option value="">Choose a request...</option>';
    requests.forEach(request => {
      const option = document.createElement('option');
      option.value = request.id;
      option.textContent = `${request.id} - ${request.name} (${request.location})`;
      requestSelect.appendChild(option);
    });
  }
  
  if (updateBtn) {
    // Handle status update
    updateBtn.addEventListener('click', () => {
      const requestId = requestSelect ? requestSelect.value : '';
      const newStatus = statusSelect ? statusSelect.value : '';
      
      if (requestId && newStatus) {
        const success = dataService.updateRequestStatus(requestId, newStatus);
        if (success) {
          alert('Request status updated successfully!');
          loadAdminData(); // Reload data
          if (requestSelect) requestSelect.value = '';
          if (statusSelect) statusSelect.value = '';
          updateBtn.disabled = true;
        } else {
          alert('Failed to update request status');
        }
      } else {
        alert('Please select both a request and a new status');
      }
    });
    
    // Enable/disable update button based on selections
    function updateButtonState() {
      updateBtn.disabled = !(requestSelect && requestSelect.value) || !(statusSelect && statusSelect.value);
    }
    
    if (requestSelect) requestSelect.addEventListener('change', updateButtonState);
    if (statusSelect) statusSelect.addEventListener('change', updateButtonState);
  }
}

// Utility functions
function showMessage(elementId, message) {
  const messageElement = document.getElementById(elementId);
  if (messageElement) {
    messageElement.textContent = message;
    messageElement.style.display = 'block';
    setTimeout(() => {
      messageElement.style.display = 'none';
    }, 5000);
  }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
  // Check if user is already logged in
  const user = dataService.getCurrentUser();
  if (user) {
    currentUser = user;
  }
  
  initNavigation();
  initForms();
  updateNavigation();
  
  // Show home page by default
  navigateToPage('home');
}); 

// Export functions for Jest testing

module.exports = {
  dataService,
  login,
  register,
  logout,
  validatePickupForm,
  validateFeedbackForm,
};

