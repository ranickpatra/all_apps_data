/* sovrn_stndalne_beacon v0.0.1 
Updated : 2017-06-01 */
window.sovrn=window.sovrn||{},sovrn.auction=sovrn.auction||{},beaconFlag=!1,sovrn.auction={doNotTrack:function(n,t){return n=n||navigator,t=t||window,optOutCookie=sovrn.auction.readCookie("tracking_optout"),"yes"===n.doNotTrack||"1"===n.doNotTrack||"1"===n.msDoNotTrack||"1"===t.doNotTrack||"1"===optOutCookie},readCookie:function(n){for(var t=n+"=",o=document.cookie.split(";"),r=0;r<o.length;r++){for(var e=o[r];" "==e.charAt(0);)e=e.substring(1,e.length);if(0==e.indexOf(t))return e.substring(t.length,e.length)}return null},sendBeacon:function(){sovrn.auction.beaconConfig=sovrn.auction.getParams(sovrn.auction.getScriptTag());try{var n,t;if(beaconFlag)return!1;n="sovrn_beacon",t=sovrn.auction.createiFrame(n,1,1),t.src=sovrn.auction.getBeaconURL(),document.body.appendChild(t),beaconFlag=!0}catch(o){return!1}return!0},getParams:function(n){var t=n.getAttribute("id"),o=document.getElementById(t);if(null==o)return!1;currentTagSRC=o.src;var r,e;return e={},r=currentTagSRC.split("?")[1]||"",(r=r.split("#")[0]||"")?(r.replace(new RegExp("([^?=&]+)(=([^&]*))?","g"),function(n,t,o,r){try{e[t]=decodeURIComponent(r)}catch(a){sovrn.ads.dbg(a)}}),e.currentTag=t,e.location=o.parentNode.nodeName,e):{}},getScriptTag:function(){var n,t,o,r=/^(https?:)?\/\/.*\.lijit\.(com|dev)\/www\/sovrn_beacon_standalone\/sovrn_standalone_beacon(\.min)?\.js/i,e=r;if("currentScript"in document&&(o=document.currentScript,o&&e.test(o.src)))return o;for(n=document.getElementsByTagName("script"),t=n.length-1;t>=0;t--)if(e.test(n[t].src))return n[t];return null},createiFrame:function(n,t,o){var r,e,a,i,c,u;r=document.createElement("iframe"),e=r.style,c={id:n,margin:"0",padding:"0",frameborder:"0",width:t+"",height:o+"",scrolling:"no",src:"about:blank"},u={margin:"0px",padding:"0px",border:"0px none",width:t+"px",height:o+"px",overflow:"hidden"};for(a in c)c.hasOwnProperty(a)&&r.setAttribute(a,c[a]);for(i in u)if(u.hasOwnProperty(i))try{e[i]=u[i]}catch(s){}return r},getBeaconURL:function(){var n=sovrn.auction.beaconConfig.hasOwnProperty("iid")?sovrn.auction.beaconConfig.iid:"";return"//gslbeacon.lijit.com/beacon?informer="+n},sovrnReady:function(n){/in/.test(document.readyState)?setTimeout("sovrn.auction.sovrnReady("+n+")",9):n()}},sovrn.auction.sovrnReady(function(){dnt=sovrn.auction.doNotTrack(),0==dnt&&sovrn.auction.sendBeacon()});