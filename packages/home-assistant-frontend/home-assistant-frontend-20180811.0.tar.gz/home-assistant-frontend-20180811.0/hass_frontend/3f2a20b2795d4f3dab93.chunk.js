/*! For license information please see 3f2a20b2795d4f3dab93.chunk.js.LICENSE */
(window.webpackJsonp=window.webpackJsonp||[]).push([[13],{150:function(e,t,a){"use strict";a(2),a(23),a(29),a(36);var s=a(4),o=a(0);Object(s.a)({_template:o["a"]`
    <style>
      :host {
        overflow: hidden; /* needed for text-overflow: ellipsis to work on ff */
        @apply --layout-vertical;
        @apply --layout-center-justified;
        @apply --layout-flex;
      }

      :host([two-line]) {
        min-height: var(--paper-item-body-two-line-min-height, 72px);
      }

      :host([three-line]) {
        min-height: var(--paper-item-body-three-line-min-height, 88px);
      }

      :host > ::slotted(*) {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      :host > ::slotted([secondary]) {
        @apply --paper-font-body1;

        color: var(--paper-item-body-secondary-color, var(--secondary-text-color));

        @apply --paper-item-body-secondary;
      }
    </style>

    <slot></slot>
`,is:"paper-item-body"})},198:function(e,t,a){"use strict";a.d(t,"b",function(){return n}),a.d(t,"a",function(){return i}),a(2);var s=a(52),o=a(1);const n={hostAttributes:{role:"dialog",tabindex:"-1"},properties:{modal:{type:Boolean,value:!1},__readied:{type:Boolean,value:!1}},observers:["_modalChanged(modal, __readied)"],listeners:{tap:"_onDialogClick"},ready:function(){this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.__readied=!0},_modalChanged:function(e,t){t&&(e?(this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.noCancelOnOutsideClick=!0,this.noCancelOnEscKey=!0,this.withBackdrop=!0):(this.noCancelOnOutsideClick=this.noCancelOnOutsideClick&&this.__prevNoCancelOnOutsideClick,this.noCancelOnEscKey=this.noCancelOnEscKey&&this.__prevNoCancelOnEscKey,this.withBackdrop=this.withBackdrop&&this.__prevWithBackdrop))},_updateClosingReasonConfirmed:function(e){this.closingReason=this.closingReason||{},this.closingReason.confirmed=e},_onDialogClick:function(e){for(var t=Object(o.b)(e).path,a=0,s=t.indexOf(this);a<s;a++){var n=t[a];if(n.hasAttribute&&(n.hasAttribute("dialog-dismiss")||n.hasAttribute("dialog-confirm"))){this._updateClosingReasonConfirmed(n.hasAttribute("dialog-confirm")),this.close(),e.stopPropagation();break}}}},i=[s.a,n]},201:function(e,t,a){"use strict";a(2),a(23),a(29),a(36),a(62);const s=document.createElement("template");s.setAttribute("style","display: none;"),s.innerHTML='<dom-module id="paper-dialog-shared-styles">\n  <template>\n    <style>\n      :host {\n        display: block;\n        margin: 24px 40px;\n\n        background: var(--paper-dialog-background-color, var(--primary-background-color));\n        color: var(--paper-dialog-color, var(--primary-text-color));\n\n        @apply --paper-font-body1;\n        @apply --shadow-elevation-16dp;\n        @apply --paper-dialog;\n      }\n\n      :host > ::slotted(*) {\n        margin-top: 20px;\n        padding: 0 24px;\n      }\n\n      :host > ::slotted(.no-padding) {\n        padding: 0;\n      }\n\n      \n      :host > ::slotted(*:first-child) {\n        margin-top: 24px;\n      }\n\n      :host > ::slotted(*:last-child) {\n        margin-bottom: 24px;\n      }\n\n      /* In 1.x, this selector was `:host > ::content h2`. In 2.x <slot> allows\n      to select direct children only, which increases the weight of this\n      selector, so we have to re-define first-child/last-child margins below. */\n      :host > ::slotted(h2) {\n        position: relative;\n        margin: 0;\n\n        @apply --paper-font-title;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-top. */\n      :host > ::slotted(h2:first-child) {\n        margin-top: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-bottom. */\n      :host > ::slotted(h2:last-child) {\n        margin-bottom: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      :host > ::slotted(.paper-dialog-buttons),\n      :host > ::slotted(.buttons) {\n        position: relative;\n        padding: 8px 8px 8px 24px;\n        margin: 0;\n\n        color: var(--paper-dialog-button-color, var(--primary-color));\n\n        @apply --layout-horizontal;\n        @apply --layout-end-justified;\n      }\n    </style>\n  </template>\n</dom-module>',document.head.appendChild(s.content)},211:function(e,t,a){"use strict";a(2);var s=a(90),o=a(198),n=(a(201),a(4)),i=a(0);Object(n.a)({_template:i["a"]`
    <style include="paper-dialog-shared-styles"></style>
    <slot></slot>
`,is:"paper-dialog",behaviors:[o.a,s.a],listeners:{"neon-animation-finish":"_onNeonAnimationFinish"},_renderOpened:function(){this.cancelAnimation(),this.playAnimation("entry")},_renderClosed:function(){this.cancelAnimation(),this.playAnimation("exit")},_onNeonAnimationFinish:function(){this.opened?this._finishRenderOpened():this._finishRenderClosed()}})},598:function(e,t,a){"use strict";a.r(t),a(152),a(151),a(149),a(150),a(102),a(53),a(117);var s=a(0),o=a(3),n=(a(127),a(116),a(13));a(211),a(128),customElements.define("ha-change-password-card",class extends o.a{static get template(){return s["a"]`
    <style include="ha-style">
      .error {
        color: red;
      }
      .status {
        color: var(--primary-color);
      }
      .error, .status {
        position: absolute;
        top: -4px;
      }
      paper-card {
        display: block;
      }
      .currentPassword {
        margin-top: -4px;
      }
    </style>
    <div>
      <paper-card heading="Change Password">
        <div class="card-content">
          <template is="dom-if" if="[[_errorMsg]]">
            <div class='error'>[[_errorMsg]]</div>
          </template>
          <template is="dom-if" if="[[_statusMsg]]">
            <div class="status">[[_statusMsg]]</div>
          </template>
          <paper-input
            class='currentPassword'
            label='Current Password'
            type='password'
            value='{{_currentPassword}}'
            required
            auto-validate
            error-message='Required'
          ></paper-input>
          <template is='dom-if' if='[[_currentPassword]]'>
            <paper-input
              label='New Password'
              type='password'
              value='{{_password1}}'
              required
              auto-validate
              error-message='Required'
            ></paper-input>
            <paper-input
              label='Confirm New Password'
              type='password'
              value='{{_password2}}'
              required
              auto-validate
              error-message='Required'
            ></paper-input>
          </template>
        </div>
        <div class="card-actions">
          <template is="dom-if" if="[[_loading]]">
            <div><paper-spinner active></paper-spinner></div>
          </template>
          <template is="dom-if" if="[[!_loading]]">
            <paper-button on-click="_changePassword">Submit</paper-button>
          </template>
        </div>
      </paper-card>
    </div>
`}static get properties(){return{hass:Object,_loading:{type:Boolean,value:!1},_statusMsg:String,_errorMsg:String,_currentPassword:String,_password1:String,_password2:String}}ready(){super.ready(),this.addEventListener("keypress",e=>{this._statusMsg=null,13===e.keyCode&&this._changePassword()})}async _changePassword(){if(this._statusMsg=null,this._currentPassword&&this._password1&&this._password2)if(this._password1===this._password2)if(this._currentPassword!==this._password1){this._loading=!0,this._errorMsg=null;try{await this.hass.callWS({type:"config/auth_provider/homeassistant/change_password",current_password:this._currentPassword,new_password:this._password1}),this.setProperties({_statusMsg:"Password changed successfully",_currentPassword:null,_password1:null,_password2:null})}catch(e){this._errorMsg=e.message}this._loading=!1}else this._errorMsg="New password must be different than current password";else this._errorMsg="New password confirmation doesn't match"}}),a(118),a(115);var i=a(14);customElements.define("ha-settings-row",class extends o.a{static get template(){return s["a"]`
    <style>
      :host {
        display: flex;
        padding: 0 16px;
        align-content: normal;
        align-self: auto;
        align-items: center;
      }
      :host([narrow]) {
        align-items: normal;
        flex-direction: column;
        border-top: 1px solid var(--divider-color);
        padding-bottom: 8px;
      }
      paper-item-body {
        padding-right: 16px;
      }
    </style>
    <paper-item-body two-line>
      <slot name="heading"></slot>
      <div secondary><slot name="description"></slot></div>
    </paper-item-body>
    <slot></slot>
    `}static get properties(){return{narrow:{type:Boolean,reflectToAttribute:!0}}}}),customElements.define("ha-pick-language-row",class extends(Object(i.a)(Object(n.a)(o.a))){static get template(){return s["a"]`
    <style>
      a { color: var(--primary-color); }
    </style>
    <ha-settings-row narrow='[[narrow]]'>
      <span slot='heading'>[[localize('ui.panel.profile.language.header')]]</span>
      <span slot='description'>
        <a
          href='https://developers.home-assistant.io/docs/en/internationalization_translation.html'
          target='_blank'>[[localize('ui.panel.profile.language.link_promo')]]</a>
      </span>
      <paper-dropdown-menu label="[[localize('ui.panel.profile.language.dropdown_label')]]" dynamic-align="">
        <paper-listbox slot="dropdown-content" attr-for-selected="language-tag" selected="{{languageSelection}}">
          <template is="dom-repeat" items="[[languages]]">
            <paper-item language-tag$="[[item.tag]]">[[item.nativeName]]</paper-item>
          </template>
        </paper-listbox>
      </paper-dropdown-menu>
    </ha-settings-row>
    `}static get properties(){return{hass:Object,narrow:Boolean,languageSelection:{type:String,observer:"languageSelectionChanged"},languages:{type:Array,computed:"computeLanguages(hass)"}}}static get observers(){return["setLanguageSelection(language)"]}computeLanguages(e){return e&&e.translationMetadata?Object.keys(e.translationMetadata.translations).map(t=>({tag:t,nativeName:e.translationMetadata.translations[t].nativeName})):[]}setLanguageSelection(e){this.languageSelection=e}languageSelectionChanged(e){e!==this.language&&this.fire("hass-language-select",{language:e})}}),customElements.define("ha-pick-theme-row",class extends(Object(i.a)(Object(n.a)(o.a))){static get template(){return s["a"]`
    <style>
      a { color: var(--primary-color); }
    </style>
    <ha-settings-row narrow='[[narrow]]'>
      <span slot='heading'>[[localize('ui.panel.profile.themes.header')]]</span>
      <span slot='description'>
        <template is='dom-if' if='[[!_hasThemes]]'>
        [[localize('ui.panel.profile.themes.error_no_theme')]]
        </template>
        <a
          href='https://www.home-assistant.io/components/frontend/#defining-themes'
          target='_blank'>[[localize('ui.panel.profile.themes.link_promo')]]</a>
      </span>
      <paper-dropdown-menu
        label="[[localize('ui.panel.profile.themes.dropdown_label')]]"
        dynamic-align
        disabled='[[!_hasThemes]]'
      >
        <paper-listbox slot="dropdown-content" selected="{{selectedTheme}}">
          <template is="dom-repeat" items="[[themes]]" as="theme">
            <paper-item>[[theme]]</paper-item>
          </template>
        </paper-listbox>
      </paper-dropdown-menu>
    </ha-settings-row>
    `}static get properties(){return{hass:Object,narrow:Boolean,_hasThemes:{type:Boolean,computed:"_compHasThemes(hass)"},themes:{type:Array,computed:"_computeThemes(hass)"},selectedTheme:{type:Number}}}static get observers(){return["selectionChanged(hass, selectedTheme)"]}_compHasThemes(e){return e.themes&&e.themes.themes&&Object.keys(e.themes.themes).length}ready(){super.ready(),this.hass.selectedTheme&&this.themes.indexOf(this.hass.selectedTheme)>0?this.selectedTheme=this.themes.indexOf(this.hass.selectedTheme):this.hass.selectedTheme||(this.selectedTheme=0)}_computeThemes(e){return e?["Backend-selected","default"].concat(Object.keys(e.themes.themes).sort()):[]}selectionChanged(e,t){t>0&&t<this.themes.length?e.selectedTheme!==this.themes[t]&&this.fire("settheme",this.themes[t]):0===t&&""!==e.selectedTheme&&this.fire("settheme","")}}),a(30),a(2);var r=a(4),l=a(1);const p=Object(r.a)({is:"iron-label",listeners:{tap:"_tapHandler"},properties:{for:{type:String,value:"",reflectToAttribute:!0,observer:"_forChanged"},_forElement:Object},attached:function(){this._forChanged()},ready:function(){this._generateLabelId()},_generateLabelId:function(){if(!this.id){var e="iron-label-"+p._labelNumber++;Object(l.b)(this).setAttribute("id",e)}},_findTarget:function(){if(this.for){var e=Object(l.b)(this).getOwnerRoot();return Object(l.b)(e).querySelector("#"+this.for)}var t=Object(l.b)(this).querySelector("[iron-label-target]");return t||(t=Object(l.b)(this).firstElementChild),t},_tapHandler:function(e){this._forElement&&Object(l.b)(e).localTarget!==this._forElement&&(this._forElement.focus(),this._forElement.click())},_applyLabelledBy:function(){this._forElement&&Object(l.b)(this._forElement).setAttribute("aria-labelledby",this.id)},_forChanged:function(){this._forElement&&Object(l.b)(this._forElement).removeAttribute("aria-labelledby"),this._forElement=this._findTarget(),this._applyLabelledBy()}});p._labelNumber=0;var d=a(129);a(157);const c="serviceWorker"in navigator&&"PushManager"in window&&("https:"===document.location.protocol||"localhost"===document.location.hostname||"127.0.0.1"===document.location.hostname);customElements.define("ha-push-notifications-toggle",class extends(Object(n.a)(o.a)){static get template(){return s["a"]`
    <paper-toggle-button
      disabled="[[_compDisabled(disabled, loading)]]"
      checked="{{pushChecked}}"
    ></paper-toggle-button>
`}static get properties(){return{hass:{type:Object,value:null},disabled:{type:Boolean,value:!1},pushChecked:{type:Boolean,value:"Notification"in window&&"granted"===Notification.permission,observer:"handlePushChange"},loading:{type:Boolean,value:!0}}}async connectedCallback(){if(super.connectedCallback(),"serviceWorker"in navigator)try{(await navigator.serviceWorker.ready).pushManager.getSubscription().then(e=>{this.loading=!1,this.pushChecked=!!e})}catch(e){}}handlePushChange(e){this.pushSupported&&(e?this.subscribePushNotifications():this.unsubscribePushNotifications())}subscribePushNotifications(){navigator.serviceWorker.ready.then(e=>e.pushManager.subscribe({userVisibleOnly:!0})).then(e=>{let t;return t=navigator.userAgent.toLowerCase().indexOf("firefox")>-1?"firefox":"chrome",this.hass.callApi("POST","notify.html5",{subscription:e,browser:t})},e=>{let t;t=e.message&&-1!==e.message.indexOf("gcm_sender_id")?"Please setup the notify.html5 platform.":"Notification registration failed.",console.error(e),this.fire("hass-notification",{message:t}),this.pushChecked=!1})}unsubscribePushNotifications(){navigator.serviceWorker.ready.then(e=>e.pushManager.getSubscription()).then(e=>e?this.hass.callApi("DELETE","notify.html5",{subscription:e}).then(()=>{e.unsubscribe()}):Promise.resolve()).catch(e=>{console.error("Error in unsub push",e),this.fire("hass-notification",{message:"Failed unsubscribing for push notifications."})})}_compDisabled(e,t){return e||t}}),customElements.define("ha-push-notifications-row",class extends(Object(i.a)(o.a)){static get template(){return s["a"]`
    <style>
      a { color: var(--primary-color); }
    </style>
    <ha-settings-row narrow='[[narrow]]'>
      <span slot='heading'>[[localize('ui.panel.profile.push_notifications.header')]]</span>
      <span
        slot='description'
      >
        [[_description(_platformLoaded, _pushSupported)]]
        <a
          href='https://www.home-assistant.io/components/notify.html5/'
          target='_blank'>[[localize('ui.panel.profile.push_notifications.link_promo')]]</a>
      </span>
      <ha-push-notifications-toggle
        hass="[[hass]]"
        disabled='[[_error]]'
      ></ha-push-notifications-toggle>
    </ha-settings-row>
    `}static get properties(){return{hass:Object,narrow:Boolean,_platformLoaded:{type:Boolean,computed:"_compPlatformLoaded(hass)"},_pushSupported:{type:Boolean,value:c},_error:{type:Boolean,computed:"_compError(_platformLoaded, _pushSupported)"}}}_compPlatformLoaded(e){return Object(d.a)(e,"notify.html5")}_compError(e,t){return!e||!t}_description(e,t){let a;return a=t?e?"description":"error_load_platform":"error_use_https",this.localize(`ui.panel.profile.push_notifications.${a}`)}}),customElements.define("ha-panel-profile",class extends(Object(n.a)(o.a)){static get template(){return s["a"]`
    <style include="ha-style">
      :host {
        -ms-user-select: initial;
        -webkit-user-select: initial;
        -moz-user-select: initial;
      }

      .content {
        display: block;
        max-width: 600px;
        margin: 0 auto;
      }

      .content > * {
        display: block;
        margin: 24px 0;
      }
    </style>

    <app-header-layout has-scrolling-region>
      <app-header slot="header" fixed>
        <app-toolbar>
          <ha-menu-button narrow='[[narrow]]' show-menu='[[showMenu]]'></ha-menu-button>
          <div main-title>Profile</div>
        </app-toolbar>
      </app-header>

      <div class='content'>
        <paper-card heading='[[hass.user.name]]'>
          <div class='card-content'>
            You are currently logged in as [[hass.user.name]].
            <template is='dom-if' if='[[hass.user.is_owner]]'>You are an owner.</template>
          </div>

          <ha-pick-language-row
            narrow="[[narrow]]"
            hass="[[hass]]"
          ></ha-pick-language-row>
          <ha-pick-theme-row
            narrow="[[narrow]]"
            hass="[[hass]]"
          ></ha-pick-theme-row>
          <ha-push-notifications-row
            narrow="[[narrow]]"
            hass="[[hass]]"
          ></ha-push-notifications-row>

          <div class='card-actions'>
            <paper-button
              class='warning'
              on-click='_handleLogOut'
            >Log out</paper-button>
          </div>
        </paper-card>

        <template is="dom-if" if="[[_canChangePassword(hass.user)]]">
          <ha-change-password-card hass="[[hass]]"></ha-change-password-card>
        </template>

      </div>
    </app-header-layout>
    `}static get properties(){return{hass:Object,narrow:Boolean,showMenu:Boolean}}_handleLogOut(){this.fire("hass-logout")}_canChangePassword(e){return e.credentials.some(e=>"homeassistant"===e.auth_provider_type)}})}}]);
//# sourceMappingURL=3f2a20b2795d4f3dab93.chunk.js.map