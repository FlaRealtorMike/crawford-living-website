/* Conversion tracking for Google Analytics 4 (added 2026-10-07).
   GA4 already counts page views (the gtag snippet in every page head). It cannot see inside the
   GoHighLevel form iframes or know that a phone number was tapped, so this reports three events:
     generate_lead   a GHL form on this page was submitted (the form's iframe posts
                     "set-sticky-contacts" to the page; sell.html relies on the same signal)
     click_to_call   a tel: link was clicked or tapped
     click_email     a mailto: link was clicked
   Nothing personal is sent to Google: no names, emails, phone numbers or addresses. Only the
   form's id and the page path. */
(function () {
  function send(name, params) {
    if (typeof window.gtag !== 'function') return;
    try { window.gtag('event', name, params); } catch (err) { /* never break the page */ }
  }

  var counted = {};
  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!Array.isArray(d) || d[0] !== 'set-sticky-contacts') return;
    var contact = null;
    try { contact = typeof d[2] === 'string' ? JSON.parse(d[2]) : d[2]; } catch (err) { return; }
    if (!contact || typeof contact !== 'object') return;

    var id = 'unknown', frames = document.getElementsByTagName('iframe');
    for (var i = 0; i < frames.length; i++) {
      if (frames[i].contentWindow === e.source) {
        id = (frames[i].getAttribute('data-layout-iframe-id') || frames[i].id || 'unknown').replace(/^inline-/, '');
        break;
      }
    }
    if (counted[id]) return;            // one lead per form per page view
    counted[id] = true;
    send('generate_lead', { form_id: id, page_path: location.pathname });
  });

  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    if (href.indexOf('tel:') === 0) send('click_to_call', { page_path: location.pathname });
    else if (href.indexOf('mailto:') === 0) send('click_email', { page_path: location.pathname });
  });
})();
