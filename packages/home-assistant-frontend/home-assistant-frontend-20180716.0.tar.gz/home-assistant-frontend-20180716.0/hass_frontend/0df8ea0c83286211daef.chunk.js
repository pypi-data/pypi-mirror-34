/*! For license information please see 0df8ea0c83286211daef.chunk.js.LICENSE */
(window.webpackJsonp=window.webpackJsonp||[]).push([[40],{196:function(e,t,n){"use strict";n.d(t,"b",function(){return s}),n.d(t,"a",function(){return o}),n(3);var i=n(41),a=n(1);const s={hostAttributes:{role:"dialog",tabindex:"-1"},properties:{modal:{type:Boolean,value:!1},__readied:{type:Boolean,value:!1}},observers:["_modalChanged(modal, __readied)"],listeners:{tap:"_onDialogClick"},ready:function(){this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.__readied=!0},_modalChanged:function(e,t){t&&(e?(this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.noCancelOnOutsideClick=!0,this.noCancelOnEscKey=!0,this.withBackdrop=!0):(this.noCancelOnOutsideClick=this.noCancelOnOutsideClick&&this.__prevNoCancelOnOutsideClick,this.noCancelOnEscKey=this.noCancelOnEscKey&&this.__prevNoCancelOnEscKey,this.withBackdrop=this.withBackdrop&&this.__prevWithBackdrop))},_updateClosingReasonConfirmed:function(e){this.closingReason=this.closingReason||{},this.closingReason.confirmed=e},_onDialogClick:function(e){for(var t=Object(a.b)(e).path,n=0,i=t.indexOf(this);n<i;n++){var s=t[n];if(s.hasAttribute&&(s.hasAttribute("dialog-dismiss")||s.hasAttribute("dialog-confirm"))){this._updateClosingReasonConfirmed(s.hasAttribute("dialog-confirm")),this.close(),e.stopPropagation();break}}}},o=[i.a,s]},201:function(e,t,n){"use strict";n(3),n(19),n(26),n(43),n(69);const i=document.createElement("template");i.setAttribute("style","display: none;"),i.innerHTML='<dom-module id="paper-dialog-shared-styles">\n  <template>\n    <style>\n      :host {\n        display: block;\n        margin: 24px 40px;\n\n        background: var(--paper-dialog-background-color, var(--primary-background-color));\n        color: var(--paper-dialog-color, var(--primary-text-color));\n\n        @apply --paper-font-body1;\n        @apply --shadow-elevation-16dp;\n        @apply --paper-dialog;\n      }\n\n      :host > ::slotted(*) {\n        margin-top: 20px;\n        padding: 0 24px;\n      }\n\n      :host > ::slotted(.no-padding) {\n        padding: 0;\n      }\n\n      \n      :host > ::slotted(*:first-child) {\n        margin-top: 24px;\n      }\n\n      :host > ::slotted(*:last-child) {\n        margin-bottom: 24px;\n      }\n\n      /* In 1.x, this selector was `:host > ::content h2`. In 2.x <slot> allows\n      to select direct children only, which increases the weight of this\n      selector, so we have to re-define first-child/last-child margins below. */\n      :host > ::slotted(h2) {\n        position: relative;\n        margin: 0;\n\n        @apply --paper-font-title;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-top. */\n      :host > ::slotted(h2:first-child) {\n        margin-top: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-bottom. */\n      :host > ::slotted(h2:last-child) {\n        margin-bottom: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      :host > ::slotted(.paper-dialog-buttons),\n      :host > ::slotted(.buttons) {\n        position: relative;\n        padding: 8px 8px 8px 24px;\n        margin: 0;\n\n        color: var(--paper-dialog-button-color, var(--primary-color));\n\n        @apply --layout-horizontal;\n        @apply --layout-end-justified;\n      }\n    </style>\n  </template>\n</dom-module>',document.head.appendChild(i.content)},216:function(e,t,n){"use strict";n(3);var i=n(80),a=n(196),s=(n(201),n(4)),o=n(0);Object(s.a)({_template:o["a"]`
    <style include="paper-dialog-shared-styles"></style>
    <slot></slot>
`,is:"paper-dialog",behaviors:[a.a,i.a],listeners:{"neon-animation-finish":"_onNeonAnimationFinish"},_renderOpened:function(){this.cancelAnimation(),this.playAnimation("entry")},_renderClosed:function(){this.cancelAnimation(),this.playAnimation("exit")},_onNeonAnimationFinish:function(){this.opened?this._finishRenderOpened():this._finishRenderClosed()}})},617:function(e,t,n){"use strict";n.r(t),n(60),n(216),n(126);var i=n(0),a=n(2),s=(n(147),n(11));customElements.define("ha-dialog-add-user",class extends(Object(s.a)(a.a)){static get template(){return i["a"]`
    <style include="ha-style-dialog">
      .error {
        color: red;
      }
      paper-dialog {
        max-width: 500px;
      }
      .username {
        margin-top: -8px;
      }
    </style>
    <paper-dialog id="dialog" with-backdrop opened="{{_opened}}" on-opened-changed="_openedChanged">
      <h2>Add user</h2>
      <div>
        <template is="dom-if" if="[[_errorMsg]]">
          <div class='error'>[[_errorMsg]]</div>
        </template>
        <paper-input
          autofocus
          class='username'
          label='Username'
          value='{{_username}}'
          required
          auto-validate
          error-message='Required'
        ></paper-input>
        <paper-input
          label='Password'
          type='password'
          value='{{_password}}'
          required
          auto-validate
          error-message='Required'
        ></paper-input>
      </div>
      <div class="buttons">
        <template is="dom-if" if="[[_loading]]">
          <div class='submit-spinner'><paper-spinner active></paper-spinner></div>
        </template>
        <template is="dom-if" if="[[!_loading]]">
          <paper-button on-click="_createUser">Create</paper-button>
        </template>
      </div>
    </paper-dialog>
`}static get properties(){return{_hass:Object,_dialogClosedCallback:Function,_loading:{type:Boolean,value:!1},_errorMsg:String,_opened:{type:Boolean,value:!1},_username:String,_password:String}}ready(){super.ready(),this.addEventListener("keypress",e=>{13===e.keyCode&&this._createUser()})}showDialog({hass:e,dialogClosedCallback:t}){this.hass=e,this._dialogClosedCallback=t,this._loading=!1,this._opened=!0}async _createUser(){if(!this._username||!this._password)return;let e;this._loading=!0,this._errorMsg=null;try{e=(await this.hass.callWS({type:"config/auth/create",name:this._username})).user.id}catch(e){return this._loading=!1,void(this._errorMsg=e.code)}try{await this.hass.callWS({type:"config/auth_provider/homeassistant/create",user_id:e,username:this._username,password:this._password})}catch(t){return this._loading=!1,this._errorMsg=t.code,void await this.hass.callWS({type:"config/auth/delete",user_id:e})}this._dialogDone(e)}_dialogDone(e){this._dialogClosedCallback({userId:e}),this.setProperties({_errorMsg:null,_username:"",_password:"",_dialogClosedCallback:null,_opened:!1})}_equals(e,t){return e===t}_openedChanged(e){this._dialogClosedCallback&&!e.detail.value&&this._dialogDone()}})}}]);
//# sourceMappingURL=0df8ea0c83286211daef.chunk.js.map