/**
 * @file pickup.test.js
 * Tests Pickup Form Validations
 */

const { fireEvent } = require('@testing-library/dom');

const html = `
<form id="pickup-form">
  <input type="text" id="fullName" required>
  <select id="location" required>
    <option value="">Select your city</option>
    <option value="Nairobi">Nairobi</option>
  </select>
  <div class="radio-group">
    <input type="radio" name="wasteType" value="General" required>
  </div>
  <button type="submit">Submit</button>
</form>
`;

beforeEach(() => {
  document.body.innerHTML = html;
  require('../script.js');
});

describe('Pickup Form Validations', () => {

  test('Full Name empty triggers validation', () => {
    const form = document.getElementById('pickup-form');
    const fullNameInput = document.getElementById('fullName');

    fireEvent.submit(form);

    expect(fullNameInput.validationMessage).toBeTruthy();
  });

  test('Location empty triggers validation', () => {
    const form = document.getElementById('pickup-form');
    const locationSelect = document.getElementById('location');

    fireEvent.submit(form);

    expect(locationSelect.validationMessage).toBeTruthy();
  });
});
