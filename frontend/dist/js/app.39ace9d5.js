webpackJsonp([1],{0:function(t,e,n){t.exports=n("x35b")},XCo1:function(t,e){},"kc+w":function(t,e){},"r+yP":function(t,e){},x35b:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s=n("/5sW"),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("div",{attrs:{id:"nav"}},[n("router-link",{attrs:{to:"/"}},[t._v("FORM BUILDER")]),t._v(" |\n    "),n("router-link",{attrs:{to:"/about"}},[t._v("PRREVIEW")])],1),t._v(" "),n("router-view")],1)},o=[],r=n("XyMi");function a(t){n("kc+w")}var l=null,c=!1,u=a,d=null,f=null,v=Object(r["a"])(l,i,o,c,u,d,f),p=v.exports,m=n("/ocq"),_=n("Z60a"),h=n.n(_),g=n("C9uT"),b=n.n(g),y=n("T/v0"),k=n.n(y),C=n("j/rp"),w=n.n(C),R=n("Oy1H"),O=n.n(R),j=n("EOM2"),F=this&&this.__decorate||function(t,e,n,s){var i,o=arguments.length,r=o<3?e:null===s?s=Object.getOwnPropertyDescriptor(e,n):s;if("object"===O()(Reflect)&&"function"===typeof Reflect.decorate)r=Reflect.decorate(t,e,n,s);else for(var a=t.length-1;a>=0;a--)(i=t[a])&&(r=(o<3?i(r):o>3?i(e,n,r):i(e,n))||r);return o>3&&r&&Object.defineProperty(e,n,r),r},x=this&&this.__metadata||function(t,e){if("object"===O()(Reflect)&&"function"===typeof Reflect.metadata)return Reflect.metadata(t,e)},P=function(t){function e(){return h()(this,e),k()(this,(e.__proto__||Object.getPrototypeOf(e)).apply(this,arguments))}return w()(e,t),e}(j["Vue"]);F([Object(j["Prop"])(),x("design:type",String)],P.prototype,"msg",void 0),F([Object(j["Prop"])({default:{}}),x("design:type",Object)],P.prototype,"rs",void 0),P=F([j["Component"]],P);var D=P,E=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("form",{staticClass:"field-segment"},[n("fieldset",[n("legend",[t._v("Form Builder")]),t._v(" "),n("div",{staticClass:"row"},[n("div",{staticClass:"column-sm-4"},[n("div",{staticClass:"input-group fluid"},[n("label",{attrs:{for:"username"}},[t._v("Field")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.rs.title,expression:"rs.title"}],attrs:{type:"text",placeholder:"Type Field Name"},domProps:{value:t.rs.title},on:{input:function(e){e.target.composing||t.$set(t.rs,"title",e.target.value)}}})])]),t._v(" "),n("div",{staticClass:"column-sm-10"},[n("div",{staticClass:"input-group fluid"},[n("label",{attrs:{for:"pwd"}},[t._v("Type")]),t._v(" "),n("select",[n("option",[t._v(t._s(t.rs.type))]),t._v(" "),n("option",[t._v("Checkbox")]),t._v(" "),n("option",[t._v("TextBox")])])])])])])])},N=[];function T(t){n("XCo1")}var $=!1,M=T,A=null,S=null,B=Object(r["a"])(D,E,N,$,M,A,S),X=B.exports,V=n("mtWM"),W=n.n(V),I=this&&this.__decorate||function(t,e,n,s){var i,o=arguments.length,r=o<3?e:null===s?s=Object.getOwnPropertyDescriptor(e,n):s;if("object"===O()(Reflect)&&"function"===typeof Reflect.decorate)r=Reflect.decorate(t,e,n,s);else for(var a=t.length-1;a>=0;a--)(i=t[a])&&(r=(o<3?i(r):o>3?i(e,n,r):i(e,n))||r);return o>3&&r&&Object.defineProperty(e,n,r),r},U=function(t){function e(){var t;return h()(this,e),t=k()(this,(e.__proto__||Object.getPrototypeOf(e)).apply(this,arguments)),t.rows=[],t.riskData={},t.selectedRisk="io",t.selectedField="",t.fieldsForRisk=[],t.tmpr={},t}return w()(e,t),b()(e,[{key:"fun",value:function(){this.rows.push({title:"",type:""})}},{key:"pushDefaultField",value:function(t){this.rows.push({title:t,type:this.riskData[this.selectedRisk]["fields"][t]["field_type"]})}},{key:"setFields",value:function(){this.fieldsForRisk=Object.keys(this.riskData[this.selectedRisk].fields)}},{key:"mounted",value:function(){this.fetchRisks()}},{key:"fetchRisks",value:function(){var t=this;W.a.get("api/v1/risk-all").then(function(e){console.log(e),t.riskData=e.data}).catch(function(t){console.log(t)})}}]),e}(j["Vue"]);U=I([Object(j["Component"])({components:{formSegment:X}})],U);var q=U,G=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"home"},[n("div",{staticClass:"container"},[n("div",{staticClass:"row"},[n("div",{staticClass:"col-sm-3"}),t._v(" "),n("div",{staticClass:"col-sm-6"},[n("form",{staticClass:"a"},[n("fieldset",[n("legend",[t._v("Form Builder")]),t._v(" "),n("div",{staticClass:"row"},[n("div",{staticClass:"column-sm-4"},[n("div",{staticClass:"input-group fluid"},[n("label",{attrs:{for:"username"}},[t._v("Risk")]),t._v(" "),n("select",{directives:[{name:"model",rawName:"v-model",value:t.selectedRisk,expression:"selectedRisk"}],on:{change:[function(e){var n=Array.prototype.filter.call(e.target.options,function(t){return t.selected}).map(function(t){var e="_value"in t?t._value:t.value;return e});t.selectedRisk=e.target.multiple?n:n[0]},t.setFields]}},t._l(t.riskData,function(e,s){return n("option",[t._v(t._s(s))])}))])]),t._v(" "),n("div",{staticClass:"column-sm-10"},[n("div",{staticClass:"input-group fluid"},[n("label",{attrs:{for:"pwd"}},[t._v("Fields For Risk")]),t._v(" "),n("select",{directives:[{name:"model",rawName:"v-model",value:t.selectedField,expression:"selectedField"}],on:{change:[function(e){var n=Array.prototype.filter.call(e.target.options,function(t){return t.selected}).map(function(t){var e="_value"in t?t._value:t.value;return e});t.selectedField=e.target.multiple?n:n[0]},function(e){t.pushDefaultField(t.selectedField)}]}},t._l(t.fieldsForRisk,function(e){return n("option",[t._v(t._s(e))])}))])])])])])])])]),t._v(" "),n("div",{staticClass:"container"},[n("div",{staticClass:"row"},[n("div",{staticClass:"col-sm-3"}),t._v(" "),n("div",{staticClass:"col-sm-6"},t._l(t.rows,function(t,e){return n("formSegment",{staticClass:"form-segment",attrs:{rs:t},on:{"update:rs":function(e){t=e}}})})),t._v(" "),n("div",{staticClass:"col-sm-3"})])]),t._v(" "),n("input",{staticClass:"button button-outline",attrs:{type:"button",value:"Add Field"},on:{click:t.fun}}),t._v(" "),n("input",{staticClass:"button button-outline",attrs:{type:"button",value:"Save Form"}})])},H=[];function J(t){n("r+yP")}var L=!1,Y=J,Z=null,z=null,K=Object(r["a"])(q,G,H,L,Y,Z,z),Q=K.exports,tt=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},et=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"about"},[n("h1",[t._v("This is an about page")])])}],nt=null,st=!1,it=null,ot=null,rt=null,at=Object(r["a"])(nt,tt,et,st,it,ot,rt),lt=at.exports;s["default"].use(m["a"]);var ct=new m["a"]({routes:[{path:"/",name:"home",component:Q},{path:"/about",name:"about",component:lt}]}),ut=n("NYxO");s["default"].use(ut["a"]);var dt=new ut["a"].Store({state:{},mutations:{},actions:{}}),ft=n("ydGU");Object(ft["a"])("".concat("/","service-worker.js"),{ready:function(){console.log("App is being served from cache by a service worker.\nFor more details, visit https://goo.gl/M232X8")},cached:function(){console.log("Content has been cached for offline use.")},updated:function(){console.log("New content is available; please refresh.")},offline:function(){console.log("No internet connection found. App is running in offline mode.")},error:function(t){console.error("Error during service worker registration:",t)}}),s["default"].config.productionTip=!1,new s["default"]({router:ct,store:dt,render:function(t){return t(p)}}).$mount("#app")}},[0]);
//# sourceMappingURL=app.39ace9d5.js.map