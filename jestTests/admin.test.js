/**
 * @file admin.test.js
 * Tests Admin Page functionalities
 */

const { fireEvent } = require('@testing-library/dom');

const html = `
<select id="requestSelect">
  <option value="">Choose a request...</option>
  <option value="REQ001">REQ001</option>
</select>
<select id="statusSelect">
  <option value="">Select status...</option>
  <option value="Completed">Completed</option>
</select>
<button id="updateStatusBtn" disabled>Update Status</button>
<table>
  <tbody id="admin-tbody">
    <tr>
      <td>REQ001</td>
      <td>John Doe</td>
      <td>Nairobi</td>
      <td>General</td>
      <td>2025-11-21</td>
      <td>Pending</td>
    </tr>
  </tbody>
</table>
`;

beforeEach(() => {
  document.body.innerHTML = html;
  require('../script.js');
});

describe('Admin Page Tests', () => {

  test('Update Status button enabled after selecting request and status', () => {
    const requestSelect = document.getElementById('requestSelect');
    const statusSelect = document.getElementById('statusSelect');
    const updateBtn = document.getElementById('updateStatusBtn');

    requestSelect.value = 'REQ001';
    fireEvent.change(requestSelect);
    statusSelect.value = 'Completed';
    fireEvent.change(statusSelect);

    expect(updateBtn.disabled).toBe(false);
  });
});
