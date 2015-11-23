(function(){
  $('body').fitText(9);
  if (window.location.protocol != "https:")
    window.location.href = "https:" + window.location.href.substring(window.location.protocol.length);
})();
