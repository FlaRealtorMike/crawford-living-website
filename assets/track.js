/* Lead tracking for Google Analytics 4 (added 2026-10-07, extended 2026-11-23).
   GA4 already counts page views (the gtag snippet in every page head). It cannot see inside the
   GoHighLevel form iframes or know that a phone number was tapped, so this reports:
     generate_lead   a lead form on this page was submitted. GHL form iframes post
                     "set-sticky-contacts" to the page; custom forms (e.g. the probate guide)
                     call window.clTrackLead(formId, formName) themselves.
     click_to_call   a tel: link was clicked or tapped
     click_email     a mailto: link was clicked
     book_click      a "Book a call" link (book.html or the GHL booking calendar) was clicked
     home_value_click  a link to the home-value page was clicked
   Every event carries the page it happened on, the visitor's first landing page and where they
   first came from (search, a referring site or a campaign tag), so a lead can be traced to the
   page and the change that produced it.
   Nothing personal is sent to Google: no names, emails, phone numbers or addresses. */
(function () {
  /* First touch: where this visitor first arrived from, kept for 90 days in this browser.
     Read by custom forms (window.clSource()) so the lead's source can travel to GoHighLevel. */
  var KEY = 'cl_first_touch', src = null;
  try { src = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (err) { src = null; }
  if (!src || !src.t || Date.now() - src.t > 90 * 864e5) {
    var q = {}, p = new URLSearchParams(location.search);
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'].forEach(function (k) {
      if (p.get(k)) q[k] = p.get(k).slice(0, 100);
    });
    var ref = '';
    try { ref = document.referrer ? new URL(document.referrer).hostname : ''; } catch (err) { ref = ''; }
    if (ref === location.hostname) ref = '';
    src = { t: Date.now(), landing: location.pathname, referrer: ref || '(direct)', utm: q };
    try { localStorage.setItem(KEY, JSON.stringify(src)); } catch (err) { /* private mode */ }
  }
  window.clSource = function () {
    return {
      page: location.pathname,
      landing_page: src.landing,
      first_referrer: src.referrer,
      first_seen: new Date(src.t).toISOString().slice(0, 10),
      utm_source: src.utm.utm_source || '',
      utm_medium: src.utm.utm_medium || '',
      utm_campaign: src.utm.utm_campaign || '',
      utm_content: src.utm.utm_content || ''
    };
  };

  function send(name, params) {
    if (typeof window.gtag !== 'function') return;
    params = params || {};
    params.page_path = location.pathname;
    params.landing_page = src.landing;
    params.first_referrer = src.referrer;
    if (src.utm.utm_campaign) params.first_campaign = src.utm.utm_campaign;
    try { window.gtag('event', name, params); } catch (err) { /* never break the page */ }
  }

  var counted = {};
  window.clTrackLead = function (id, formName) {
    if (counted[id]) return;            // one lead per form per page view
    counted[id] = true;
    send('generate_lead', { form_id: id, form_name: formName || id });
  };

  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!Array.isArray(d) || d[0] !== 'set-sticky-contacts') return;
    var contact = null;
    try { contact = typeof d[2] === 'string' ? JSON.parse(d[2]) : d[2]; } catch (err) { return; }
    if (!contact || typeof contact !== 'object') return;

    var id = 'unknown', name = '', frames = document.getElementsByTagName('iframe');
    for (var i = 0; i < frames.length; i++) {
      if (frames[i].contentWindow === e.source) {
        id = (frames[i].getAttribute('data-layout-iframe-id') || frames[i].id || 'unknown').replace(/^inline-/, '');
        name = frames[i].getAttribute('data-form-name') || '';
        break;
      }
    }
    window.clTrackLead(id, name);
  });

  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var label = (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60);
    if (href.indexOf('tel:') === 0) send('click_to_call', { link_text: label });
    else if (href.indexOf('mailto:') === 0) send('click_email', { link_text: label });
    else if (/(^|\/)book(\.html)?([?#]|$)|widget\/booking\//.test(href)) send('book_click', { link_text: label });
    else if (/(^|\/)home-value(\.html)?([?#]|$)/.test(href)) send('home_value_click', { link_text: label });
  });
})();
