(window.webpackJsonp=window.webpackJsonp||[]).push([[13],{608:function(e,a,t){"use strict";t.r(a),t(151),t(150),t(148),t(60),t(116);var s=t(0),n=t(3),o=(t(127),t(149),t(15));customElements.define("ha-panel-profile",class extends(Object(o.a)(n.a)){static get template(){return s["a"]`
    <style include="ha-style">
      :host {
        -ms-user-select: initial;
        -webkit-user-select: initial;
        -moz-user-select: initial;
      }

      paper-card {
        display: block;
        max-width: 600px;
        margin: 16px auto;
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
          <div class='card-actions'>
            <paper-button
              class='warning'
              on-click='_handleLogOut'
            >Log out</paper-button>
          </div>
        </paper-card>
      </div>
    </app-header-layout>
    `}static get properties(){return{hass:Object,narrow:Boolean,showMenu:Boolean}}_handleLogOut(){this.fire("hass-logout")}})}}]);
//# sourceMappingURL=9daa6074aa7f6ea3c5b9.chunk.js.map