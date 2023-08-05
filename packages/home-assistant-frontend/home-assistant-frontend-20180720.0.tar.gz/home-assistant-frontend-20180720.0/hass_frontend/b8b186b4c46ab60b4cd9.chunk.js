/*! For license information please see b8b186b4c46ab60b4cd9.chunk.js.LICENSE */
(window.webpackJsonp=window.webpackJsonp||[]).push([[34],{221:function(e,t,a){"use strict";a(2),a(25),a(40);var o=a(94),i=(a(119),a(4)),n=a(0);Object(i.a)({_template:n["a"]`
    <style include="paper-item-shared-styles"></style>
    <style>
      :host {
        @apply --layout-horizontal;
        @apply --layout-center;
        @apply --paper-font-subhead;

        @apply --paper-item;
        @apply --paper-icon-item;
      }

      .content-icon {
        @apply --layout-horizontal;
        @apply --layout-center;

        width: var(--paper-item-icon-width, 56px);
        @apply --paper-item-icon;
      }
    </style>

    <div id="contentIcon" class="content-icon">
      <slot name="item-icon"></slot>
    </div>
    <slot></slot>
`,is:"paper-icon-item",behaviors:[o.a]})},607:function(e,t,a){"use strict";a.r(t),a(115),a(30),a(59),a(221),a(101),a(114);var o=a(0),i=a(3),n=(a(88),a(124),a(75)),l=a(18);customElements.define("ha-sidebar",class extends(Object(l.a)(Object(n.a)(i.a))){static get template(){return o["a"]`
    <style include="iron-flex iron-flex-alignment iron-positioning">
      :host {
        --sidebar-text: {
          color: var(--sidebar-text-color);
          font-weight: 500;
          font-size: 14px;
        };
        height: 100%;
        display: block;
        overflow: auto;
        -ms-user-select: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        border-right: 1px solid var(--divider-color);
        background-color: var(--sidebar-background-color, var(--primary-background-color));
      }

      app-toolbar {
        font-weight: 400;
        color: var(--primary-text-color);
        border-bottom: 1px solid var(--divider-color);
        background-color: var(--primary-background-color);
      }

      paper-listbox {
        padding-bottom: 0;
      }

      paper-icon-item {
        --paper-icon-item: {
          cursor: pointer;
        };

        --paper-item-icon: {
          color: var(--sidebar-icon-color);
        };
      }

      paper-icon-item.iron-selected {
        --paper-icon-item: {
          background-color: var(--sidebar-selected-background-color, var(--paper-grey-200));
        };

        --paper-item-icon: {
          color: var(--sidebar-selected-icon-color);
        };
      }

      paper-icon-item .item-text {
        @apply --sidebar-text;
      }
      paper-icon-item.iron-selected .item-text {
          color: var(--sidebar-selected-text-color);
      }

      paper-icon-item.logout {
        margin-top: 16px;
      }

      .divider {
        height: 1px;
        background-color: var(--divider-color);
        margin: 4px 0;
      }

      .setting {
        @apply --sidebar-text;
      }

      .subheader {
        @apply --sidebar-text;
        padding: 16px;
      }

      .dev-tools {
        color: var(--sidebar-icon-color);
        padding: 0 8px;
      }
    </style>

    <app-toolbar>
      <div main-title="">Home Assistant</div>
      <paper-icon-button icon="hass:chevron-left" hidden$="[[narrow]]" on-click="toggleMenu"></paper-icon-button>
    </app-toolbar>

    <paper-listbox attr-for-selected="data-panel" selected="[[hass.panelUrl]]">
      <paper-icon-item on-click="menuClicked" data-panel$="[[defaultPage]]">
        <ha-icon slot="item-icon" icon="hass:apps"></ha-icon>
        <span class="item-text">[[localize('panel.states')]]</span>
      </paper-icon-item>

      <template is="dom-repeat" items="[[panels]]">
        <paper-icon-item on-click="menuClicked">
          <ha-icon slot="item-icon" icon="[[item.icon]]"></ha-icon>
          <span class="item-text">[[computePanelName(localize, item)]]</span>
        </paper-icon-item>
      </template>

      <template is='dom-if' if='[[!hass.user]]'>
        <paper-icon-item on-click="menuClicked" data-panel="logout" class="logout">
          <ha-icon slot="item-icon" icon="hass:exit-to-app"></ha-icon>
          <span class="item-text">[[localize('ui.sidebar.log_out')]]</span>
        </paper-icon-item>
      </template>
      <template is='dom-if' if='[[hass.user]]'>
        <paper-icon-item on-click="menuClicked" data-panel="profile">
          <ha-icon slot="item-icon" icon="hass:account"></ha-icon>
          <span class="item-text">[[_computeUserName(hass.user)]]</span>
        </paper-icon-item>
      </template>
    </paper-listbox>

    <div>
      <div class="divider"></div>

      <div class="subheader">[[localize('ui.sidebar.developer_tools')]]</div>

      <div class="dev-tools layout horizontal justified">
        <paper-icon-button icon="hass:remote" data-panel="dev-service" alt="[[localize('panel.dev-services')]]" title="[[localize('panel.dev-services')]]" on-click="menuClicked"></paper-icon-button>
        <paper-icon-button icon="hass:code-tags" data-panel="dev-state" alt="[[localize('panel.dev-states')]]" title="[[localize('panel.dev-states')]]" on-click="menuClicked"></paper-icon-button>
        <paper-icon-button icon="hass:radio-tower" data-panel="dev-event" alt="[[localize('panel.dev-events')]]" title="[[localize('panel.dev-events')]]" on-click="menuClicked"></paper-icon-button>
        <paper-icon-button icon="hass:file-xml" data-panel="dev-template" alt="[[localize('panel.dev-templates')]]" title="[[localize('panel.dev-templates')]]" on-click="menuClicked"></paper-icon-button>
        <template is="dom-if" if="[[_mqttLoaded(hass)]]">
          <paper-icon-button icon="hass:altimeter" data-panel="dev-mqtt" alt="[[localize('panel.dev-mqtt')]]" title="[[localize('panel.dev-mqtt')]]" on-click="menuClicked"></paper-icon-button>
        </template>
        <paper-icon-button icon="hass:information-outline" data-panel="dev-info" alt="[[localize('panel.dev-info')]]" title="[[localize('panel.dev-info')]]" on-click="menuClicked"></paper-icon-button>
      </div>
    </div>
`}static get properties(){return{hass:{type:Object},menuShown:{type:Boolean},menuSelected:{type:String},narrow:Boolean,panels:{type:Array,computed:"computePanels(hass)"},defaultPage:String}}_mqttLoaded(e){return-1!==e.config.core.components.indexOf("mqtt")}_computeUserName(e){return e&&(e.name||"Unnamed User")}computePanelName(e,t){return e(`panel.${t.title}`)||t.title}computePanels(e){var t=e.panels,a={map:1,logbook:2,history:3},o=[];return Object.keys(t).forEach(function(e){t[e].title&&o.push(t[e])}),o.sort(function(e,t){var o=e.component_name in a,i=t.component_name in a;return o&&i?a[e.component_name]-a[t.component_name]:o?-1:i?1:e.title<t.title?-1:e.title>t.title?1:0}),o}menuClicked(e){if(e.model)return void this.selectPanel(e.model.item.url_path);let t,a=e.target,o=5;do{t=a.getAttribute("data-panel"),a=a.parentElement,o--}while(o>0&&null!==a&&!t);o>0&&null!==a&&this.selectPanel(t)}toggleMenu(){this.fire("hass-close-menu")}selectPanel(e){if("logout"!==e){var t="/"+e;t!==document.location.pathname&&this.navigate(t)}else this.handleLogOut()}handleLogOut(){this.fire("hass-logout")}})}}]);
//# sourceMappingURL=b8b186b4c46ab60b4cd9.chunk.js.map