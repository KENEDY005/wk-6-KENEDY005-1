/**
 * @file login.test.js
 * Tests Login Form Validations
 */

const { fireEvent } = require('@testing-library/dom');

const html = `
<form id="login-form">
  <input type="email" id="login-email" required>
  <input type="password" id="login-password" required>
  <div id="login-error"></div>
  <button type="submit">Sign In</button>
</form>
`;

beforeEach(() => {
  document.body.innerHTML = html;
  require('../script.js');
});

describe('Login Form Validations', () => {

  test('Email empty triggers validation', () => {
    const form = document.getElementById('login-form');
    const emailInput = document.getElementById('login-email');

    fireEvent.submit(form);

    expect(emailInput.validationMessage).toBeTruthy();
  });

  test('Password empty triggers validation', () => {
    const form = document.getElementById('login-form');
    const passwordInput = document.getElementById('login-password');

    fireEvent.submit(form);

    expect(passwordInput.validationMessage).toBeTruthy();
  });
});
