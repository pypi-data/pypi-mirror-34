(window.webpackJsonp=window.webpackJsonp||[]).push([[28],{131:function(e,t,n){"use strict";function r(e,t){"setProperties"in e?e.setProperties(t):Object.keys(t).forEach(function(n){e[n]=t[n]})}n.d(t,"a",function(){return r})},132:function(e,t,n){"use strict";function r(e){var t="html_url"in e?"ha-panel-"+e.name:e.name;return document.createElement(t)}n.d(t,"a",function(){return r})},133:function(e,t,n){"use strict";n.d(t,"a",function(){return a});var r=n(70),o=function(e,t){if(Array.isArray(e))return e;if(Symbol.iterator in Object(e))return function(e,t){var n=[],r=!0,o=!1,i=void 0;try{for(var a,s=e[Symbol.iterator]();!(r=(a=s.next()).done)&&(n.push(a.value),!t||n.length!==t);r=!0);}catch(e){o=!0,i=e}finally{try{!r&&s.return&&s.return()}finally{if(o)throw i}}return n}(e,t);throw new TypeError("Invalid attempt to destructure non-iterable instance")},i={};function a(e){if(e.html_url){var t=[n.e(40).then(n.bind(null,73))];return e.embed_iframe||t.push(Promise.all([n.e(10),n.e(39)]).then(n.bind(null,129))),Promise.all(t).then(function(t){return(0,o(t,1)[0].importHrefPromise)(e.html_url)})}return e.js_url?(e.js_url in i||(i[e.js_url]=Object(r.a)(e.js_url)),i[e.js_url]):Promise.reject("No valid url found in panel config.")}},616:function(e,t,n){"use strict";n.r(t);var r=n(2),o=n(12),i=n(68),a=n(133),s=n(132),u=n(131),c=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),l=function(e){function t(){!function(e,n){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this);var e=function(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}(this,(t.__proto__||Object.getPrototypeOf(t)).call(this));return e._setProperties=null,e}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}(t,Object(i.a)(Object(o.a)(r.a))),c(t,null,[{key:"properties",get:function(){return{hass:Object,narrow:Boolean,showMenu:Boolean,route:Object,panel:{type:Object,observer:"_panelChanged"}}}},{key:"observers",get:function(){return["_dataChanged(hass, narrow, showMenu, route)"]}}]),c(t,[{key:"_panelChanged",value:function(e){var t=this;for(delete window.customPanel,this._setProperties=null;this.lastChild;)this.remove(this.lastChild);var n=e.config._panel_custom,r=document.createElement("a");if(r.href=n.html_url||n.js_url,n.trust_external||["localhost","127.0.0.1",location.hostname].includes(r.hostname)||confirm('Do you trust the external panel "'+n.name+'" at "'+r.href+'"?\n\nIt will have access to all data in Home Assistant.\n\n(Check docs for the panel_custom component to hide this message)'))if(n.embed_iframe){window.customPanel=this,this.innerHTML="\n    <style>\n      iframe {\n        border: 0;\n        width: 100%;\n        height: 100%;\n        display: block;\n      }\n    </style>\n    <iframe></iframe>\n    ";var o=this.querySelector("iframe").contentWindow.document;o.open(),o.write("<script src='/frontend_es5/custom-panel.js'><\/script>"),o.close()}else Object(a.a)(n).then(function(){var r=Object(s.a)(n);t._setProperties=function(e){return Object(u.a)(r,e)},Object(u.a)(r,{panel:e,hass:t.hass,narrow:t.narrow,showMenu:t.showMenu,route:t.route}),t.appendChild(r)},function(){alert("Unable to load custom panel from "+r.href)})}},{key:"disconnectedCallback",value:function(){(function e(t,n,r){null===t&&(t=Function.prototype);var o=Object.getOwnPropertyDescriptor(t,n);if(void 0===o){var i=Object.getPrototypeOf(t);return null===i?void 0:e(i,n,r)}if("value"in o)return o.value;var a=o.get;return void 0!==a?a.call(r):void 0})(t.prototype.__proto__||Object.getPrototypeOf(t.prototype),"disconnectedCallback",this).call(this),delete window.customPanel}},{key:"_dataChanged",value:function(e,t,n,r){this._setProperties&&this._setProperties({hass:e,narrow:t,showMenu:n,route:r})}},{key:"registerIframe",value:function(e,t){e(this.panel,{hass:this.hass,narrow:this.narrow,showMenu:this.showMenu,route:this.route}),this._setProperties=t}}]),t}();customElements.define("ha-panel-custom",l)},70:function(e,t,n){"use strict";function r(e,t,n){return new Promise(function(r,o){var i=document.createElement(e),a="src",s="body";switch(i.onload=function(){return r(t)},i.onerror=function(){return o(t)},e){case"script":i.async=!0,n&&(i.type=n);break;case"link":i.type="text/css",i.rel="stylesheet",a="href",s="head"}i[a]=t,document[s].appendChild(i)})}n.d(t,"a",function(){return o}),n.d(t,"b",function(){return i});var o=function(e){return r("script",e)},i=function(e){return r("script",e,"module")}}}]);
//# sourceMappingURL=eef2ad2f618b81eeb707.chunk.js.map