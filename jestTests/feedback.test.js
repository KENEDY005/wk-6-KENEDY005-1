/**
 * CleanCity Feedback Form Tests
 * Tests actual JS behaviour instead of HTML5 browser validation
 */

const fs = require('fs');
const path = require('path');
const { fireEvent } = require('@testing-library/dom');

// Load main HTML (where the feedback form lives)
const html = fs.readFileSync(path.resolve(__dirname, '../index.html'), 'utf8');

describe('Feedback Form Validations', () => {
  let form, requestId, reason, comments, success, errorBox;

  beforeEach(() => {
    document.documentElement.innerHTML = html.toString();

    // Load your script.js so event listeners run
    jest.resetModules();
    require('../script.js');

    form = document.getElementById('feedback-form');
    requestId = document.getElementById('requestId');
    reason = document.getElementById('reason');
    comments = document.getElementById('comments');
    success = document.getElementById('feedback-success');
  });

  /**
   * NEGATIVE TEST 1
   * No validationMessage here — instead your JS probably stops submission silently.
   * So we check that success message does NOT appear.
   */
  test('Request ID empty should prevent success message', () => {
    requestId.value = "";
    reason.value = "Missed Pickup";

    fireEvent.submit(form);

    expect(success.style.display).toBe("none");
  });

  /**
   * NEGATIVE TEST 2
   */
  test('Reason empty should prevent success message', () => {
    requestId.value = "REQ1001";
    reason.value = "";

    fireEvent.submit(form);

    expect(success.style.display).toBe("none");
  });

  /**
   * POSITIVE TEST
   */
  test('Successful submission shows thank you message', () => {
    requestId.value = "REQ1001";
    reason.value = "Missed Pickup";
    comments.value = "Test comment";

    fireEvent.submit(form);

    expect(success.style.display).toBe("block");
    expect(success.textContent).toContain("Thank you for your feedback");
  });
});
