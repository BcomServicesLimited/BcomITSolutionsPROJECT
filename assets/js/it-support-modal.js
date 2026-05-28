(function () {
  var overlay = document.getElementById('bcItSupportModal');
  if (!overlay) return;

  var closeBtn     = document.getElementById('bcModalClose');
  var form         = document.getElementById('bcItSupportForm');
  var submitBtn    = document.getElementById('bcSubmitBtn');
  var formWrap     = document.getElementById('bcFormWrap');
  var success      = document.getElementById('bcFormSuccess');
  var successPhone = document.getElementById('bcSuccessPhone');

  document.addEventListener('click', function (e) {
    if (e.target.closest('.bcom-request-btn')) {
      e.preventDefault();
      overlay.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      var nameField = document.getElementById('bcName');
      if (nameField) nameField.focus();
    }
  });

  function closeModal() {
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) closeModal();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeModal();
  });

  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var name  = document.getElementById('bcName').value.trim();
    var phone = document.getElementById('bcPhone').value.trim();
    var email = document.getElementById('bcEmail').value.trim();
    var type  = document.getElementById('bcIssueType').value;
    var desc  = document.getElementById('bcDescription').value.trim();

    if (!name || !phone || !email || !type || !desc) {
      alert('Please fill in all required fields.');
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending...';

    fetch('https://formspree.io/f/xreoqepk', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        name: name,
        phone: phone,
        email: email,
        issue_type: type,
        description: desc,
        _subject: 'IT Support Request — ' + type + ' — ' + name,
        _replyto: email
      })
    })
      .then(function (res) {
        if (res.ok) {
          formWrap.style.display = 'none';
          success.style.display = 'block';
          successPhone.textContent = phone;
        } else {
          throw new Error('Network response was not ok');
        }
      })
      .catch(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Request a Callback →';
        alert('Something went wrong. Please call us directly on 07 3041 8993.');
      });
  });
})();
