/**
 * @file registration.test.js
 * Tests Registration Form Validations
 */

const { fireEvent } = require('@testing-library/dom');

const html = `
<form id="register-form">
  <input type="text" id="register-name" required>
  <input type="email" id="register-email" required>
  <input type="password" id="register-password" required>
  <input type="password" id="register-confirm-password" required>
  <button type="submit">Register</button>
</form>
`;

beforeEach(() => {
  document.body.innerHTML = html;
  require('../script.js');
});

describe('Registration Form Validations', () => {

  test('Email without @ triggers validation', () => {
    const form = document.getElementById('register-form');
    const emailInput = document.getElementById('register-email');

    emailInput.value = 'usercleancity.com';

    fireEvent.submit(form);

    expect(emailInput.validationMessage).toBeTruthy();
  });

  test('Password confirmation required', () => {
    const form = document.getElementById('register-form');
    const confirmPassword = document.getElementById('register-confirm-password');

    fireEvent.submit(form);

    expect(confirmPassword.validationMessage).toBeTruthy();
  });
});
