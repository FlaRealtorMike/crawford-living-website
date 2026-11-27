/* reveal the timeline and step cards once, when they scroll into view. */
(function(){
  if(!('IntersectionObserver' in window))return;
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  document.documentElement.classList.add('anim');
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.25});
  document.querySelectorAll('.tl,.hs').forEach(function(el){io.observe(el)});
})();
