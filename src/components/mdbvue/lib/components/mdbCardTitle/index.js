(function(e,t){"object"===typeof exports&&"object"===typeof module?module.exports=t():"function"===typeof define&&define.amd?define([],t):"object"===typeof exports?exports["mdbCardTitle"]=t():e["mdbCardTitle"]=t()})("undefined"!==typeof self?self:this,(function(){return function(e){var t={};function n(r){if(t[r])return t[r].exports;var o=t[r]={i:r,l:!1,exports:{}};return e[r].call(o.exports,o,o.exports,n),o.l=!0,o.exports}return n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)n.d(r,o,function(t){return e[t]}.bind(null,o));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s="fb15")}({8875:function(e,t,n){var r,o,i;(function(n,c){o=[],r=c,i="function"===typeof r?r.apply(t,o):r,void 0===i||(e.exports=i)})("undefined"!==typeof self&&self,(function(){function e(){if(document.currentScript)return document.currentScript;try{throw new Error}catch(s){var e,t,n,r=/.*at [^(]*\((.*):(.+):(.+)\)$/gi,o=/@([^@]*):(\d+):(\d+)\s*$/gi,i=r.exec(s.stack)||o.exec(s.stack),c=i&&i[1]||!1,u=i&&i[2]||!1,f=document.location.href.replace(document.location.hash,""),a=document.getElementsByTagName("script");c===f&&(e=document.documentElement.outerHTML,t=new RegExp("(?:[^\\n]+?\\n){0,"+(u-2)+"}[^<]*<script>([\\d\\D]*?)<\\/script>[\\d\\D]*","i"),n=e.replace(t,"$1").trim());for(var d=0;d<a.length;d++){if("interactive"===a[d].readyState)return a[d];if(a[d].src===c)return a[d];if(c===f&&a[d].innerHTML&&a[d].innerHTML.trim()===n)return a[d]}return null}}return e}))},fb15:function(e,t,n){"use strict";if(n.r(t),n.d(t,"mdbCardTitle",(function(){return f})),"undefined"!==typeof window){var r=window.document.currentScript,o=n("8875");r=o(),"currentScript"in document||Object.defineProperty(document,"currentScript",{get:o});var i=r&&r.src.match(/(.+\/)[^/]+\.js(\?.*)?$/);i&&(n.p=i[1])}var c=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n(e.tag,{tag:"component",class:e.className},[e._t("default")],2)},u=[],f={props:{tag:{type:String,default:"h4"}},computed:{className:function(){return["card-title"]}}},a=f,d=a;function s(e,t,n,r,o,i,c,u){var f,a="function"===typeof e?e.options:e;if(t&&(a.render=t,a.staticRenderFns=n,a._compiled=!0),r&&(a.functional=!0),i&&(a._scopeId="data-v-"+i),c?(f=function(e){e=e||this.$vnode&&this.$vnode.ssrContext||this.parent&&this.parent.$vnode&&this.parent.$vnode.ssrContext,e||"undefined"===typeof __VUE_SSR_CONTEXT__||(e=__VUE_SSR_CONTEXT__),o&&o.call(this,e),e&&e._registeredComponents&&e._registeredComponents.add(c)},a._ssrRegister=f):o&&(f=u?function(){o.call(this,this.$root.$options.shadowRoot)}:o),f)if(a.functional){a._injectStyles=f;var d=a.render;a.render=function(e,t){return f.call(t),d(e,t)}}else{var s=a.beforeCreate;a.beforeCreate=s?[].concat(s,f):[f]}return{exports:e,options:a}}var l=s(d,c,u,!1,null,"6dbf9a14",null),p=l.exports;t["default"]=p}})["default"]}));
//# sourceMappingURL=index.umd.min.js.map