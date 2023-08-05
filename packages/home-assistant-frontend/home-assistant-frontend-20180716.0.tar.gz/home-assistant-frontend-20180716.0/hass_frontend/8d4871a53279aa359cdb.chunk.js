/*! For license information please see 8d4871a53279aa359cdb.chunk.js.LICENSE */
(window.webpackJsonp=window.webpackJsonp||[]).push([[32],{152:function(e,t,a){"use strict";a(115);const i=customElements.get("paper-slider");customElements.define("ha-paper-slider",class extends i{static get template(){const e=document.createElement("template");e.innerHTML=i.template.innerHTML;const t=e.content.querySelector("style");return t.setAttribute("include","paper-slider"),t.innerHTML="\n      .pin > .slider-knob > .slider-knob-inner {\n        font-size:  var(--ha-paper-slider-pin-font-size, 10px);\n        line-height: normal;\n      }\n\n      .pin > .slider-knob > .slider-knob-inner::before {\n        top: unset;\n        margin-left: unset;\n\n        bottom: calc(15px + var(--calculated-paper-slider-height)/2);\n        left: 50%;\n        width: 2.2em;\n        height: 2.2em;\n\n        -webkit-transform-origin: left bottom;\n        transform-origin: left bottom;\n        -webkit-transform: rotate(-45deg) scale(0) translate(0);\n        transform: rotate(-45deg) scale(0) translate(0);\n      }\n\n      .pin.expand > .slider-knob > .slider-knob-inner::before {\n        -webkit-transform: rotate(-45deg) scale(1) translate(7px, -7px);\n        transform: rotate(-45deg) scale(1) translate(7px, -7px);\n      }\n\n      .pin > .slider-knob > .slider-knob-inner::after {\n        top: unset;\n        font-size: unset;\n\n        bottom: calc(15px + var(--calculated-paper-slider-height)/2);\n        left: 50%;\n        margin-left: -1.1em;\n        width: 2.2em;\n        height: 2.1em;\n\n        -webkit-transform-origin: center bottom;\n        transform-origin: center bottom;\n        -webkit-transform: scale(0) translate(0);\n        transform: scale(0) translate(0);\n      }\n\n      .pin.expand > .slider-knob > .slider-knob-inner::after {\n        -webkit-transform: scale(1) translate(0, -10px);\n        transform: scale(1) translate(0, -10px);\n      }\n    ",e}})},196:function(e,t,a){"use strict";a.d(t,"b",function(){return r}),a.d(t,"a",function(){return o}),a(3);var i=a(41),s=a(1);const r={hostAttributes:{role:"dialog",tabindex:"-1"},properties:{modal:{type:Boolean,value:!1},__readied:{type:Boolean,value:!1}},observers:["_modalChanged(modal, __readied)"],listeners:{tap:"_onDialogClick"},ready:function(){this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.__readied=!0},_modalChanged:function(e,t){t&&(e?(this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.noCancelOnOutsideClick=!0,this.noCancelOnEscKey=!0,this.withBackdrop=!0):(this.noCancelOnOutsideClick=this.noCancelOnOutsideClick&&this.__prevNoCancelOnOutsideClick,this.noCancelOnEscKey=this.noCancelOnEscKey&&this.__prevNoCancelOnEscKey,this.withBackdrop=this.withBackdrop&&this.__prevWithBackdrop))},_updateClosingReasonConfirmed:function(e){this.closingReason=this.closingReason||{},this.closingReason.confirmed=e},_onDialogClick:function(e){for(var t=Object(s.b)(e).path,a=0,i=t.indexOf(this);a<i;a++){var r=t[a];if(r.hasAttribute&&(r.hasAttribute("dialog-dismiss")||r.hasAttribute("dialog-confirm"))){this._updateClosingReasonConfirmed(r.hasAttribute("dialog-confirm")),this.close(),e.stopPropagation();break}}}},o=[i.a,r]},201:function(e,t,a){"use strict";a(3),a(19),a(26),a(43),a(69);const i=document.createElement("template");i.setAttribute("style","display: none;"),i.innerHTML='<dom-module id="paper-dialog-shared-styles">\n  <template>\n    <style>\n      :host {\n        display: block;\n        margin: 24px 40px;\n\n        background: var(--paper-dialog-background-color, var(--primary-background-color));\n        color: var(--paper-dialog-color, var(--primary-text-color));\n\n        @apply --paper-font-body1;\n        @apply --shadow-elevation-16dp;\n        @apply --paper-dialog;\n      }\n\n      :host > ::slotted(*) {\n        margin-top: 20px;\n        padding: 0 24px;\n      }\n\n      :host > ::slotted(.no-padding) {\n        padding: 0;\n      }\n\n      \n      :host > ::slotted(*:first-child) {\n        margin-top: 24px;\n      }\n\n      :host > ::slotted(*:last-child) {\n        margin-bottom: 24px;\n      }\n\n      /* In 1.x, this selector was `:host > ::content h2`. In 2.x <slot> allows\n      to select direct children only, which increases the weight of this\n      selector, so we have to re-define first-child/last-child margins below. */\n      :host > ::slotted(h2) {\n        position: relative;\n        margin: 0;\n\n        @apply --paper-font-title;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-top. */\n      :host > ::slotted(h2:first-child) {\n        margin-top: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-bottom. */\n      :host > ::slotted(h2:last-child) {\n        margin-bottom: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      :host > ::slotted(.paper-dialog-buttons),\n      :host > ::slotted(.buttons) {\n        position: relative;\n        padding: 8px 8px 8px 24px;\n        margin: 0;\n\n        color: var(--paper-dialog-button-color, var(--primary-color));\n\n        @apply --layout-horizontal;\n        @apply --layout-end-justified;\n      }\n    </style>\n  </template>\n</dom-module>',document.head.appendChild(i.content)},224:function(e,t,a){"use strict";a(3),a(19);var i=a(196),s=(a(26),a(4)),r=a(0);Object(s.a)({_template:r["a"]`
    <style>

      :host {
        display: block;
        @apply --layout-relative;
      }

      :host(.is-scrolled:not(:first-child))::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: var(--divider-color);
      }

      :host(.can-scroll:not(.scrolled-to-bottom):not(:last-child))::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: var(--divider-color);
      }

      .scrollable {
        padding: 0 24px;

        @apply --layout-scroll;
        @apply --paper-dialog-scrollable;
      }

      .fit {
        @apply --layout-fit;
      }
    </style>

    <div id="scrollable" class="scrollable" on-scroll="updateScrollState">
      <slot></slot>
    </div>
`,is:"paper-dialog-scrollable",properties:{dialogElement:{type:Object}},get scrollTarget(){return this.$.scrollable},ready:function(){this._ensureTarget(),this.classList.add("no-padding")},attached:function(){this._ensureTarget(),requestAnimationFrame(this.updateScrollState.bind(this))},updateScrollState:function(){this.toggleClass("is-scrolled",this.scrollTarget.scrollTop>0),this.toggleClass("can-scroll",this.scrollTarget.offsetHeight<this.scrollTarget.scrollHeight),this.toggleClass("scrolled-to-bottom",this.scrollTarget.scrollTop+this.scrollTarget.offsetHeight>=this.scrollTarget.scrollHeight)},_ensureTarget:function(){this.dialogElement=this.dialogElement||this.parentElement,this.dialogElement&&this.dialogElement.behaviors&&this.dialogElement.behaviors.indexOf(i.b)>=0?(this.dialogElement.sizingTarget=this.scrollTarget,this.scrollTarget.classList.remove("fit")):this.dialogElement&&this.scrollTarget.classList.add("fit")}})},259:function(e,t,a){"use strict";const i={DOMAIN_DEVICE_CLASS:{binary_sensor:["battery","cold","connectivity","door","garage_door","gas","heat","light","lock","moisture","motion","moving","occupancy","opening","plug","power","presence","problem","safety","smoke","sound","vibration","window"],cover:["garage"],sensor:["battery","humidity","illuminance","temperature"]},UNKNOWN_TYPE:"json",ADD_TYPE:"key-value",TYPE_TO_TAG:{string:"ha-customize-string",json:"ha-customize-string",icon:"ha-customize-icon",boolean:"ha-customize-boolean",array:"ha-customize-array","key-value":"ha-customize-key-value"}};i.LOGIC_STATE_ATTRIBUTES=i.LOGIC_STATE_ATTRIBUTES||{entity_picture:void 0,friendly_name:{type:"string",description:"Name"},icon:{type:"icon"},emulated_hue:{type:"boolean",domains:["emulated_hue"]},emulated_hue_name:{type:"string",domains:["emulated_hue"]},haaska_hidden:void 0,haaska_name:void 0,homebridge_hidden:{type:"boolean"},homebridge_name:{type:"string"},supported_features:void 0,attribution:void 0,custom_ui_more_info:{type:"string"},custom_ui_state_card:{type:"string"},device_class:{type:"array",options:i.DOMAIN_DEVICE_CLASS,description:"Device class",domains:["binary_sensor","cover","sensor"]},hidden:{type:"boolean",description:"Hide from UI"},assumed_state:{type:"boolean",domains:["switch","light","cover","climate","fan","group"]},initial_state:{type:"string",domains:["automation"]},unit_of_measurement:{type:"string"}},t.a=i},267:function(e,t,a){"use strict";var i=a(6),s=a(196),r=a(44),o=a(12);t.a=Object(i.a)(e=>(class extends(Object(r.b)([o.a,s.a],e)){static get properties(){return{withBackdrop:{type:Boolean,value:!0}}}}))},596:function(e,t,a){"use strict";a.r(t),a(201),a(224);var i=a(0),s=a(2),r=(a(147),a(104),a(50),a(156),a(158),a(157),a(25),a(60),a(59),a(12)),o=a(11);customElements.define("more-info-alarm_control_panel",class extends(Object(o.a)(Object(r.a)(s.a))){static get template(){return i["a"]`
      <style include="iron-flex"></style>
      <style>
        paper-input {
          margin: auto;
          max-width: 200px;
        }
        .pad {
          display: flex;
          justify-content: center;
          margin-bottom: 24px;
        }
        .pad div {
          display: flex;
          flex-direction: column;
        }
        .pad paper-button {
          width: 80px;
        }
        .actions paper-button {
          min-width: 160px;
          margin-bottom: 16px;
          color: var(--primary-color);
        }
        paper-button.disarm {
          color: var(--google-red-500);
        }
      </style>

      <template is="dom-if" if="[[_codeFormat]]">
        <paper-input
          label="[[localize('ui.card.alarm_control_panel.code')]]"
          value="{{_enteredCode}}"
          type="password"
          disabled="[[!_inputEnabled]]"
        ></paper-input>

        <template is="dom-if" if="[[_isNumber(_codeFormat)]]">
          <div class="pad">
            <div>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="1" raised>1</paper-button>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="4" raised>4</paper-button>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="7" raised>7</paper-button>
            </div>
            <div>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="2" raised>2</paper-button>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="5" raised>5</paper-button>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="8" raised>8</paper-button>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="0" raised>0</paper-button>
            </div>
            <div>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="3" raised>3</paper-button>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="6" raised>6</paper-button>
              <paper-button on-click='_digitClicked' disabled='[[!_inputEnabled]]' data-digit="9" raised>9</paper-button>
              <paper-button on-click='_clearEnteredCode' disabled='[[!_inputEnabled]]' raised>
                [[localize('ui.card.alarm_control_panel.clear_code')]]
              </paper-button>
            </div>
          </div>
        </template>
      </template>

      <div class="layout horizontal center-justified actions">
        <template is="dom-if" if="[[_disarmVisible]]">
          <paper-button raised class="disarm" on-click="_callService" data-service="alarm_disarm" disabled="[[!_codeValid]]">
            [[localize('ui.card.alarm_control_panel.disarm')]]
          </paper-button>
        </template>
        <template is="dom-if" if="[[_armVisible]]">
          <paper-button raised on-click="_callService" data-service="alarm_arm_home" disabled="[[!_codeValid]]">
            [[localize('ui.card.alarm_control_panel.arm_home')]]
          </paper-button>
          <paper-button raised on-click="_callService" data-service="alarm_arm_away" disabled="[[!_codeValid]]">
            [[localize('ui.card.alarm_control_panel.arm_away')]]
          </paper-button>
        </template>
      </div>
    `}static get properties(){return{hass:Object,stateObj:{type:Object,observer:"_stateObjChanged"},_enteredCode:{type:String,value:""},_codeFormat:{type:String,value:""},_codeValid:{type:Boolean,computed:"_validateCode(_enteredCode, _codeFormat)"},_disarmVisible:{type:Boolean,value:!1},_armVisible:{type:Boolean,value:!1},_inputEnabled:{type:Boolean,value:!1}}}constructor(){super(),this._armedStates=["armed_home","armed_away","armed_night","armed_custom_bypass"]}_stateObjChanged(e,t){if(e){const t=e.state,a={_codeFormat:e.attributes.code_format,_armVisible:"disarmed"===t,_disarmVisible:this._armedStates.includes(t)||"pending"===t||"triggered"===t};a._inputEnabled=a._disarmVisible||a._armVisible,this.setProperties(a)}t&&setTimeout(()=>{this.fire("iron-resize")},500)}_isNumber(e){return"Number"===e}_validateCode(e,t){return!t||e.length>0}_digitClicked(e){this._enteredCode+=e.target.getAttribute("data-digit")}_clearEnteredCode(){this._enteredCode=""}_callService(e){const t=e.target.getAttribute("data-service"),a={entity_id:this.stateObj.entity_id,code:this._enteredCode};this.hass.callService("alarm_control_panel",t,a).then(()=>{this._enteredCode=""})}}),a(155),customElements.define("more-info-automation",class extends(Object(o.a)(s.a)){static get template(){return i["a"]`
      <style>
        paper-button {
          color: var(--primary-color);
          font-weight: 500;
        }
        .flex {
          display: flex;
          justify-content: space-between;
        }
        .actions {
          margin: 36px 0 8px 0;
          text-align: right;
        }
      </style>

      <div class="flex">
        <div>
          [[localize('ui.card.automation.last_triggered')]]:
        </div>
        <ha-relative-time hass="[[hass]]" datetime="[[stateObj.attributes.last_triggered]]"></ha-relative-time>
      </div>

      <div class="actions">
        <paper-button on-click="handleTriggerTapped">
          [[localize('ui.card.automation.trigger')]]
        </paper-button>
      </div>
    `}static get properties(){return{hass:Object,stateObj:Object}}handleTriggerTapped(){this.hass.callService("automation","trigger",{entity_id:this.stateObj.entity_id})}});var n=a(16);customElements.define("more-info-camera",class extends(Object(r.a)(s.a)){static get template(){return i["a"]`
    <style>
      :host {
        max-width:640px;
      }

      .camera-image {
        width: 100%;
      }
    </style>

    <img class="camera-image" src="[[computeCameraImageUrl(hass, stateObj, isVisible)]]" on-load="imageLoaded" alt="[[_computeStateName(stateObj)]]">
`}static get properties(){return{hass:{type:Object},stateObj:{type:Object},isVisible:{type:Boolean,value:!0}}}connectedCallback(){super.connectedCallback(),this.isVisible=!0}disconnectedCallback(){this.isVisible=!1,super.disconnectedCallback()}imageLoaded(){this.fire("iron-resize")}_computeStateName(e){return Object(n.a)(e)}computeCameraImageUrl(e,t,a){return e.demo?"/demo/webcam.jpg":t&&a?"/api/camera_proxy_stream/"+t.entity_id+"?token="+t.attributes.access_token:"data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"}}),a(105),a(87),a(103),a(154);var l=a(7),d=a(17);customElements.define("ha-climate-control",class extends(Object(r.a)(s.a)){static get template(){return i["a"]`
    <style include="iron-flex iron-flex-alignment"></style>
    <style>
      /* local DOM styles go here */
      :host {
        @apply --layout-flex;
        @apply --layout-horizontal;
        @apply --layout-justified;
      }
      .in-flux#target_temperature {
        color: var(--google-red-500);
      }
      #target_temperature {
        @apply --layout-self-center;
        font-size: 200%;
      }
      .control-buttons {
        font-size: 200%;
        text-align: right;
      }
      paper-icon-button {
        height: 48px;
        width: 48px;
      }
    </style>

    <!-- local DOM goes here -->
    <div id="target_temperature">
      [[value]] [[units]]
    </div>
    <div class="control-buttons">
      <div>
        <paper-icon-button icon="hass:chevron-up" on-click="incrementValue"></paper-icon-button>
      </div>
      <div>
        <paper-icon-button icon="hass:chevron-down" on-click="decrementValue"></paper-icon-button>
      </div>
    </div>
`}static get properties(){return{value:{type:Number,observer:"valueChanged"},units:{type:String},min:{type:Number},max:{type:Number},step:{type:Number,value:1}}}temperatureStateInFlux(e){this.$.target_temperature.classList.toggle("in-flux",e)}incrementValue(){const e=this.value+this.step;this.value<this.max&&(this.last_changed=Date.now(),this.temperatureStateInFlux(!0)),e<=this.max?e<=this.min?this.value=this.min:this.value=e:this.value=this.max}decrementValue(){const e=this.value-this.step;this.value>this.min&&(this.last_changed=Date.now(),this.temperatureStateInFlux(!0)),e>=this.min?this.value=e:this.value=this.min}valueChanged(){this.last_changed&&window.setTimeout(()=>{Date.now()-this.last_changed>=2e3&&(this.fire("change"),this.temperatureStateInFlux(!1),this.last_changed=null)},2010)}}),a(152);var p=a(90);function c(e,t){if(!e||!e.attributes.supported_features)return"";const a=e.attributes.supported_features;return Object.keys(t).map(e=>0!=(a&e)?t[e]:"").filter(e=>""!==e).join(" ")}customElements.define("more-info-climate",class extends(Object(o.a)(Object(r.a)(s.a))){static get template(){return i["a"]`
    <style include="iron-flex"></style>
    <style>
      :host {
        color: var(--primary-text-color);
      }

      .container-on,
      .container-away_mode,
      .container-aux_heat,
      .container-temperature,
      .container-humidity,
      .container-operation_list,
      .container-fan_list,
      .container-swing_list {
        display: none;
      }

      .has-on .container-on,
      .has-away_mode .container-away_mode,
      .has-aux_heat .container-aux_heat,
      .has-target_temperature .container-temperature,
      .has-target_temperature_low .container-temperature,
      .has-target_temperature_high .container-temperature,
      .has-target_humidity .container-humidity,
      .has-operation_mode .container-operation_list,
      .has-fan_mode .container-fan_list,
      .has-swing_list .container-swing_list,
      .has-swing_mode .container-swing_list {
        display: block;
        margin-bottom: 5px;
      }

      .container-operation_list iron-icon,
      .container-fan_list iron-icon,
      .container-swing_list iron-icon {
        margin: 22px 16px 0 0;
      }

      paper-dropdown-menu {
        width: 100%;
      }

      paper-item {
        cursor: pointer;
      }

      ha-paper-slider {
        width: 100%;
      }

      .container-humidity .single-row {
          display: flex;
          height: 50px;
      }

      .target-humidity {
        width: 90px;
        font-size: 200%;
        margin: auto;
      }

      ha-climate-control.range-control-left,
      ha-climate-control.range-control-right {
        float: left;
        width: 46%;
      }
      ha-climate-control.range-control-left {
        margin-right: 4%;
      }
      ha-climate-control.range-control-right {
        margin-left: 4%;
      }

      .humidity {
        --paper-slider-active-color: var(--paper-blue-400);
        --paper-slider-secondary-color: var(--paper-blue-400);
      }

      .single-row {
        padding: 8px 0;
      }
      }
    </style>

    <div class$="[[computeClassNames(stateObj)]]">

      <template is="dom-if" if="[[supportsOn(stateObj)]]">
        <div class="container-on">
          <div class="center horizontal layout single-row">
            <div class="flex">[[localize('ui.card.climate.on_off')]]</div>
            <paper-toggle-button checked="[[onToggleChecked]]" on-change="onToggleChanged">
            </paper-toggle-button>
          </div>
        </div>
      </template>

      <div class="container-temperature">
        <div class$="[[stateObj.attributes.operation_mode]]">
          <div hidden$="[[!supportsTemperatureControls(stateObj)]]">[[localize('ui.card.climate.target_temperature')]]</div>
          <template is="dom-if" if="[[supportsTemperature(stateObj)]]">
            <ha-climate-control value="[[stateObj.attributes.temperature]]" units="[[stateObj.attributes.unit_of_measurement]]" step="[[computeTemperatureStepSize(stateObj)]]" min="[[stateObj.attributes.min_temp]]" max="[[stateObj.attributes.max_temp]]" on-change="targetTemperatureChanged">
            </ha-climate-control>
          </template>
          <template is="dom-if" if="[[supportsTemperatureRange(stateObj)]]">
            <ha-climate-control value="[[stateObj.attributes.target_temp_low]]" units="[[stateObj.attributes.unit_of_measurement]]" step="[[computeTemperatureStepSize(stateObj)]]" min="[[stateObj.attributes.min_temp]]" max="[[stateObj.attributes.target_temp_high]]" class="range-control-left" on-change="targetTemperatureLowChanged">
            </ha-climate-control>
            <ha-climate-control value="[[stateObj.attributes.target_temp_high]]" units="[[stateObj.attributes.unit_of_measurement]]" step="[[computeTemperatureStepSize(stateObj)]]" min="[[stateObj.attributes.target_temp_low]]" max="[[stateObj.attributes.max_temp]]" class="range-control-right" on-change="targetTemperatureHighChanged">
            </ha-climate-control>
          </template>
        </div>
      </div>

      <template is="dom-if" if="[[supportsHumidity(stateObj)]]">
        <div class="container-humidity">
          <div>[[localize('ui.card.climate.target_humidity')]]</div>
            <div class="single-row">
              <div class="target-humidity">[[stateObj.attributes.humidity]] %</div>
              <ha-paper-slider class="humidity" min="[[stateObj.attributes.min_humidity]]" max="[[stateObj.attributes.max_humidity]]" secondary-progress="[[stateObj.attributes.max_humidity]]" step="1" pin="" value="[[stateObj.attributes.humidity]]" on-change="targetHumiditySliderChanged" ignore-bar-touch="">
              </ha-paper-slider>
          </div>
        </div>
      </template>

      <template is="dom-if" if="[[supportsOperationMode(stateObj)]]">
        <div class="container-operation_list">
          <div class="controls">
            <paper-dropdown-menu label-float="" dynamic-align="" label="[[localize('ui.card.climate.operation')]]">
              <paper-listbox slot="dropdown-content" selected="{{operationIndex}}">
                <template is="dom-repeat" items="[[stateObj.attributes.operation_list]]" on-dom-change="handleOperationListUpdate">
                  <paper-item>[[_localizeOperationMode(localize, item)]]</paper-item>
                </template>
              </paper-listbox>
            </paper-dropdown-menu>
          </div>
        </div>
      </template>

      <template is="dom-if" if="[[supportsFanMode(stateObj)]]">
        <div class="container-fan_list">
          <paper-dropdown-menu label-float="" dynamic-align="" label="[[localize('ui.card.climate.fan_mode')]]">
            <paper-listbox slot="dropdown-content" selected="{{fanIndex}}">
              <template is="dom-repeat" items="[[stateObj.attributes.fan_list]]" on-dom-change="handleFanListUpdate">
                <paper-item>[[item]]</paper-item>
              </template>
            </paper-listbox>
          </paper-dropdown-menu>
        </div>
      </template>

      <template is="dom-if" if="[[supportsSwingMode(stateObj)]]">
        <div class="container-swing_list">
          <paper-dropdown-menu label-float="" dynamic-align="" label="[[localize('ui.card.climate.swing_mode')]]">
            <paper-listbox slot="dropdown-content" selected="{{swingIndex}}">
              <template is="dom-repeat" items="[[stateObj.attributes.swing_list]]" on-dom-change="handleSwingListUpdate">
                <paper-item>[[item]]</paper-item>
              </template>
            </paper-listbox>
          </paper-dropdown-menu>
        </div>
      </template>

      <template is="dom-if" if="[[supportsAwayMode(stateObj)]]">
        <div class="container-away_mode">
          <div class="center horizontal layout single-row">
            <div class="flex">[[localize('ui.card.climate.away_mode')]]</div>
            <paper-toggle-button checked="[[awayToggleChecked]]" on-change="awayToggleChanged">
            </paper-toggle-button>
          </div>
        </div>
      </template>

      <template is="dom-if" if="[[supportsAuxHeat(stateObj)]]">
        <div class="container-aux_heat">
          <div class="center horizontal layout single-row">
            <div class="flex">[[localize('ui.card.climate.aux_heat')]]</div>
            <paper-toggle-button checked="[[auxToggleChecked]]" on-change="auxToggleChanged">
            </paper-toggle-button>
          </div>
        </div>
      </template>
    </div>
`}static get properties(){return{hass:{type:Object},stateObj:{type:Object,observer:"stateObjChanged"},operationIndex:{type:Number,value:-1,observer:"handleOperationmodeChanged"},fanIndex:{type:Number,value:-1,observer:"handleFanmodeChanged"},swingIndex:{type:Number,value:-1,observer:"handleSwingmodeChanged"},awayToggleChecked:Boolean,auxToggleChecked:Boolean,onToggleChecked:Boolean}}stateObjChanged(e,t){e&&this.setProperties({awayToggleChecked:"on"===e.attributes.away_mode,auxToggleChecked:"on"===e.attributes.aux_heat,onToggleChecked:"off"!==e.state}),t&&(this._debouncer=d.a.debounce(this._debouncer,l.timeOut.after(500),()=>{this.fire("iron-resize")}))}handleOperationListUpdate(){this.operationIndex=-1,this.stateObj.attributes.operation_list&&(this.operationIndex=this.stateObj.attributes.operation_list.indexOf(this.stateObj.attributes.operation_mode))}handleSwingListUpdate(){this.swingIndex=-1,this.stateObj.attributes.swing_list&&(this.swingIndex=this.stateObj.attributes.swing_list.indexOf(this.stateObj.attributes.swing_mode))}handleFanListUpdate(){this.fanIndex=-1,this.stateObj.attributes.fan_list&&(this.fanIndex=this.stateObj.attributes.fan_list.indexOf(this.stateObj.attributes.fan_mode))}computeTemperatureStepSize(e){return e.attributes.target_temp_step?e.attributes.target_temp_step:-1!==e.attributes.unit_of_measurement.indexOf("F")?1:.5}supportsTemperatureControls(e){return this.supportsTemperature(e)||this.supportsTemperatureRange(e)}supportsTemperature(e){return 0!=(1&e.attributes.supported_features)&&"number"==typeof e.attributes.temperature}supportsTemperatureRange(e){return 0!=(6&e.attributes.supported_features)&&("number"==typeof e.attributes.target_temp_low||"number"==typeof e.attributes.target_temp_high)}supportsHumidity(e){return 0!=(8&e.attributes.supported_features)}supportsFanMode(e){return 0!=(64&e.attributes.supported_features)}supportsOperationMode(e){return 0!=(128&e.attributes.supported_features)}supportsSwingMode(e){return 0!=(512&e.attributes.supported_features)}supportsAwayMode(e){return 0!=(1024&e.attributes.supported_features)}supportsAuxHeat(e){return 0!=(2048&e.attributes.supported_features)}supportsOn(e){return 0!=(4096&e.attributes.supported_features)}computeClassNames(e){var t=[Object(p.a)(e,["current_temperature","current_humidity"]),c(e,{1:"has-target_temperature",2:"has-target_temperature_high",4:"has-target_temperature_low",8:"has-target_humidity",16:"has-target_humidity_high",32:"has-target_humidity_low",64:"has-fan_mode",128:"has-operation_mode",256:"has-hold_mode",512:"has-swing_mode",1024:"has-away_mode",2048:"has-aux_heat",4096:"has-on"})];return t.push("more-info-climate"),t.join(" ")}targetTemperatureChanged(e){const t=e.target.value;t!==this.stateObj.attributes.temperature&&this.callServiceHelper("set_temperature",{temperature:t})}targetTemperatureLowChanged(e){const t=e.currentTarget.value;t!==this.stateObj.attributes.target_temp_low&&this.callServiceHelper("set_temperature",{target_temp_low:t,target_temp_high:this.stateObj.attributes.target_temp_high})}targetTemperatureHighChanged(e){const t=e.currentTarget.value;t!==this.stateObj.attributes.target_temp_high&&this.callServiceHelper("set_temperature",{target_temp_low:this.stateObj.attributes.target_temp_low,target_temp_high:t})}targetHumiditySliderChanged(e){const t=e.target.value;t!==this.stateObj.attributes.humidity&&this.callServiceHelper("set_humidity",{humidity:t})}awayToggleChanged(e){const t="on"===this.stateObj.attributes.away_mode,a=e.target.checked;t!==a&&this.callServiceHelper("set_away_mode",{away_mode:a})}auxToggleChanged(e){const t="on"===this.stateObj.attributes.aux_heat,a=e.target.checked;t!==a&&this.callServiceHelper("set_aux_heat",{aux_heat:a})}onToggleChanged(e){const t="off"!==this.stateObj.state,a=e.target.checked;t!==a&&this.callServiceHelper(a?"turn_on":"turn_off",{})}handleFanmodeChanged(e){if(""===e||-1===e)return;const t=this.stateObj.attributes.fan_list[e];t!==this.stateObj.attributes.fan_mode&&this.callServiceHelper("set_fan_mode",{fan_mode:t})}handleOperationmodeChanged(e){if(""===e||-1===e)return;const t=this.stateObj.attributes.operation_list[e];t!==this.stateObj.attributes.operation_mode&&this.callServiceHelper("set_operation_mode",{operation_mode:t})}handleSwingmodeChanged(e){if(""===e||-1===e)return;const t=this.stateObj.attributes.swing_list[e];t!==this.stateObj.attributes.swing_mode&&this.callServiceHelper("set_swing_mode",{swing_mode:t})}callServiceHelper(e,t){t.entity_id=this.stateObj.entity_id,this.hass.callService("climate",e,t).then(()=>{this.stateObjChanged(this.stateObj)})}_localizeOperationMode(e,t){return e(`state.climate.${t}`)||t}}),a(120),a(126),a(153),customElements.define("more-info-configurator",class extends s.a{static get template(){return i["a"]`
    <style include="iron-flex"></style>
    <style>
      p {
        margin: 8px 0;
      }

      a {
        color: var(--primary-color);
      }

      p > img {
        max-width: 100%;
      }

      p.center {
        text-align: center;
      }

      p.error {
        color: #C62828;
      }

      p.submit {
        text-align: center;
        height: 41px;
      }

      paper-spinner {
        width: 14px;
        height: 14px;
        margin-right: 20px;
      }

      [hidden] {
        display: none;
      }
    </style>

    <div class="layout vertical">
      <template is="dom-if" if="[[isConfigurable]]">
        <ha-markdown content="[[stateObj.attributes.description]]"></ha-markdown>

        <p class="error" hidden$="[[!stateObj.attributes.errors]]">
          [[stateObj.attributes.errors]]
        </p>

        <template is="dom-repeat" items="[[stateObj.attributes.fields]]">
          <paper-input label="[[item.name]]" name="[[item.id]]" type="[[item.type]]" on-change="fieldChanged"></paper-input>
        </template>

        <p class="submit" hidden$="[[!stateObj.attributes.submit_caption]]">
          <paper-button raised="" disabled="[[isConfiguring]]" on-click="submitClicked">
            <paper-spinner active="[[isConfiguring]]" hidden="[[!isConfiguring]]" alt="Configuring"></paper-spinner>
            [[stateObj.attributes.submit_caption]]
          </paper-button>

        </p>

      </template>
    </div>
`}static get properties(){return{stateObj:{type:Object},action:{type:String,value:"display"},isConfigurable:{type:Boolean,computed:"computeIsConfigurable(stateObj)"},isConfiguring:{type:Boolean,value:!1},fieldInput:{type:Object,value:function(){return{}}}}}computeIsConfigurable(e){return"configure"===e.state}fieldChanged(e){var t=e.target;this.fieldInput[t.name]=t.value}submitClicked(){var e={configure_id:this.stateObj.attributes.configure_id,fields:this.fieldInput};this.isConfiguring=!0,this.hass.callService("configurator","configure",e).then(function(){this.isConfiguring=!1}.bind(this),function(){this.isConfiguring=!1}.bind(this))}}),a(170),a(77),customElements.define("ha-labeled-slider",class extends s.a{static get template(){return i["a"]`
    <style>
      :host {
        display: block;
        padding-bottom: 16px;
      }

      .title {
        margin-bottom: 16px;
        opacity: var(--dark-primary-opacity);
      }

      ha-icon {
        float: left;
        margin-top: 4px;
        opacity: var(--dark-secondary-opacity);
      }

      ha-paper-slider {
        background-image: var(--ha-slider-background);
      }
    </style>

    <div class="title">[[caption]]</div>
    <div class="extra-container">
      <slot name="extra"></slot>
    </div>
    <div class="slider-container">
      <ha-icon icon="[[icon]]" hidden$="[[!icon]]"></ha-icon>
      <ha-paper-slider
        min="[[min]]" max="[[max]]" step="[[step]]"
        pin="[[pin]]" disabled="[[disabled]]" disabled="[[disabled]]"
        value="{{value}}"
      ></ha-paper-slider>
    </div>
`}static get properties(){return{caption:String,disabled:Boolean,min:Number,max:Number,pin:Boolean,step:Number,extra:{type:Boolean,value:!1},ignoreBarTouch:{type:Boolean,value:!0},icon:{type:String,value:""},value:{type:Number,notify:!0}}}});var u=a(73);const h={128:"has-set_tilt_position"};customElements.define("more-info-cover",class extends(Object(o.a)(s.a)){static get template(){return i["a"]`
  <style include="iron-flex"></style>
  <style>
    .current_position, .tilt {
      max-height: 0px;
      overflow: hidden;
    }

    .has-current_position .current_position,
    .has-set_tilt_position .tilt,
    .has-current_tilt_position .tilt
    {
      max-height: 208px;
    }

    [invisible] {
      visibility: hidden !important;
    }
  </style>
  <div class$="[[computeClassNames(stateObj)]]">

    <div class="current_position">
      <ha-labeled-slider
        caption="[[localize('ui.card.cover.position')]]" pin=""
        value="{{coverPositionSliderValue}}"
        disabled="[[!entityObj.supportsSetPosition]]"
        on-change="coverPositionSliderChanged"
      ></ha-labeled-slider>
    </div>

    <div class="tilt">
      <ha-labeled-slider
        caption="[[localize('ui.card.cover.tilt_position')]]" pin="" extra=""
        value="{{coverTiltPositionSliderValue}}"
        disabled="[[!entityObj.supportsSetTiltPosition]]"
        on-change="coverTiltPositionSliderChanged">

        <ha-cover-tilt-controls
          slot="extra" hidden$="[[entityObj.isTiltOnly]]"
          hass="[[hass]]" state-obj="[[stateObj]]"
        ></ha-cover-tilt-controls>

      </ha-labeled-slider>
    </div>

  </div>
`}static get properties(){return{hass:Object,stateObj:{type:Object,observer:"stateObjChanged"},entityObj:{type:Object,computed:"computeEntityObj(hass, stateObj)"},coverPositionSliderValue:Number,coverTiltPositionSliderValue:Number}}computeEntityObj(e,t){return new u.a(e,t)}stateObjChanged(e){e&&this.setProperties({coverPositionSliderValue:e.attributes.current_position,coverTiltPositionSliderValue:e.attributes.current_tilt_position})}computeClassNames(e){return[Object(p.a)(e,["current_position","current_tilt_position"]),c(e,h)].join(" ")}coverPositionSliderChanged(e){this.entityObj.setCoverPosition(e.target.value)}coverTiltPositionSliderChanged(e){this.entityObj.setCoverTiltPosition(e.target.value)}});var m=a(259);customElements.define("ha-attributes",class extends s.a{static get template(){return i["a"]`
    <style include="iron-flex iron-flex-alignment"></style>
    <style>
      .data-entry .value {
        max-width: 200px;
      }
      .attribution {
        color: var(--secondary-text-color);
        text-align: right;
      }
    </style>

    <div class="layout vertical">
      <template is="dom-repeat" items="[[computeDisplayAttributes(stateObj, filtersArray)]]" as="attribute">
        <div class="data-entry layout justified horizontal">
          <div class="key">[[formatAttribute(attribute)]]</div>
          <div class="value">[[formatAttributeValue(stateObj, attribute)]]</div>
        </div>
      </template>
      <div class="attribution" hidden$="[[!computeAttribution(stateObj)]]">[[computeAttribution(stateObj)]]</div>
    </div>
`}static get properties(){return{stateObj:{type:Object},extraFilters:{type:String,value:""},filtersArray:{type:Array,computed:"computeFiltersArray(extraFilters)"}}}computeFiltersArray(e){return Object.keys(m.a.LOGIC_STATE_ATTRIBUTES).concat(e?e.split(","):[])}computeDisplayAttributes(e,t){return e?Object.keys(e.attributes).filter(function(e){return-1===t.indexOf(e)}):[]}formatAttribute(e){return e.replace(/_/g," ")}formatAttributeValue(e,t){var a=e.attributes[t];return null===a?"-":Array.isArray(a)?a.join(", "):a instanceof Object?JSON.stringify(a,null,2):a}computeAttribution(e){return e.attributes.attribution}}),customElements.define("more-info-default",class extends s.a{static get template(){return i["a"]`
    <ha-attributes state-obj="[[stateObj]]"></ha-attributes>
`}static get properties(){return{stateObj:{type:Object}}}}),customElements.define("more-info-fan",class extends(Object(o.a)(Object(r.a)(s.a))){static get template(){return i["a"]`
    <style include="iron-flex"></style>
    <style>
      .container-speed_list,
      .container-direction,
      .container-oscillating {
        display: none;
      }

      .has-speed_list .container-speed_list,
      .has-direction .container-direction,
      .has-oscillating .container-oscillating {
        display: block;
      }

      paper-dropdown-menu {
        width: 100%;
      }

      paper-item {
        cursor: pointer;
      }
    </style>

    <div class$="[[computeClassNames(stateObj)]]">

      <div class="container-speed_list">
        <paper-dropdown-menu label-float="" dynamic-align="" label="[[localize('ui.card.fan.speed')]]">
          <paper-listbox slot="dropdown-content" selected="{{speedIndex}}">
            <template is="dom-repeat" items="[[stateObj.attributes.speed_list]]">
              <paper-item>[[item]]</paper-item>
            </template>
          </paper-listbox>
        </paper-dropdown-menu>
      </div>

      <div class="container-oscillating">
        <div class="center horizontal layout single-row">
          <div class="flex">[[localize('ui.card.fan.oscillate')]]</div>
          <paper-toggle-button checked="[[oscillationToggleChecked]]" on-change="oscillationToggleChanged">
          </paper-toggle-button>
        </div>
      </div>

      <div class="container-direction">
        <div class="direction">
          <div>[[localize('ui.card.fan.direction')]]</div>
          <paper-icon-button icon="hass:rotate-left" on-click="onDirectionLeft" title="Left" disabled="[[computeIsRotatingLeft(stateObj)]]"></paper-icon-button>
          <paper-icon-button icon="hass:rotate-right" on-click="onDirectionRight" title="Right" disabled="[[computeIsRotatingRight(stateObj)]]"></paper-icon-button>
        </div>
      </div>
    </div>

    <ha-attributes state-obj="[[stateObj]]" extra-filters="speed,speed_list,oscillating,direction"></ha-attributes>
`}static get properties(){return{hass:{type:Object},stateObj:{type:Object,observer:"stateObjChanged"},speedIndex:{type:Number,value:-1,observer:"speedChanged"},oscillationToggleChecked:{type:Boolean}}}stateObjChanged(e,t){e&&this.setProperties({oscillationToggleChecked:e.attributes.oscillating,speedIndex:e.attributes.speed_list?e.attributes.speed_list.indexOf(e.attributes.speed):-1}),t&&setTimeout(()=>{this.fire("iron-resize")},500)}computeClassNames(e){return"more-info-fan "+Object(p.a)(e,["oscillating","speed_list","direction"])}speedChanged(e){var t;""!==e&&-1!==e&&(t=this.stateObj.attributes.speed_list[e])!==this.stateObj.attributes.speed&&this.hass.callService("fan","turn_on",{entity_id:this.stateObj.entity_id,speed:t})}oscillationToggleChanged(e){var t=this.stateObj.attributes.oscillating,a=e.target.checked;t!==a&&this.hass.callService("fan","oscillate",{entity_id:this.stateObj.entity_id,oscillating:a})}onDirectionLeft(){this.hass.callService("fan","set_direction",{entity_id:this.stateObj.entity_id,direction:"reverse"})}onDirectionRight(){this.hass.callService("fan","set_direction",{entity_id:this.stateObj.entity_id,direction:"forward"})}computeIsRotatingLeft(e){return"reverse"===e.attributes.direction}computeIsRotatingRight(e){return"forward"===e.attributes.direction}});var b=a(1),g=a(15),v=a(72),y=a(134);customElements.define("more-info-group",class extends s.a{static get template(){return i["a"]`
    <style>
      .child-card {
        margin-bottom: 8px;
      }

      .child-card:last-child {
        margin-bottom: 0;
      }
    </style>

    <div id="groupedControlDetails"></div>
    <template is="dom-repeat" items="[[states]]" as="state">
      <div class="child-card">
        <state-card-content state-obj="[[state]]" hass="[[hass]]"></state-card-content>
      </div>
    </template>
`}static get properties(){return{hass:{type:Object},stateObj:{type:Object},states:{type:Array,computed:"computeStates(stateObj, hass)"}}}static get observers(){return["statesChanged(stateObj, states)"]}computeStates(e,t){for(var a=[],i=e.attributes.entity_id,s=0;s<i.length;s++){var r=t.states[i[s]];r&&a.push(r)}return a}statesChanged(e,t){let a=!1;if(t&&t.length>0){const i=t.find(e=>"on"===e.state)||t[0],s=Object(g.a)(i);if("group"!==s){a=Object.assign({},i,{entity_id:e.entity_id,attributes:Object.assign({},i.attributes)});for(let e=0;e<t.length;e++)if(s!==Object(g.a)(t[e])){a=!1;break}}}if(a)Object(v.a)(this.$.groupedControlDetails,"MORE-INFO-"+Object(y.a)(a).toUpperCase(),{stateObj:a,hass:this.hass});else{const e=Object(b.b)(this.$.groupedControlDetails);e.lastChild&&e.removeChild(e.lastChild)}}}),a(169),customElements.define("more-info-history_graph",class extends s.a{static get template(){return i["a"]`
    <style>
    :host {
      display: block;
      margin-bottom: 6px;
    }
    </style>
    <ha-history_graph-card hass="[[hass]]" state-obj="[[stateObj]]" in-dialog="">
    <ha-attributes state-obj="[[stateObj]]"></ha-attributes>
  </ha-history_graph-card>
`}static get properties(){return{hass:Object,stateObj:Object}}}),a(3),a(265),customElements.define("paper-time-input",class extends s.a{static get template(){return i["a"]`
      <style>
        :host {
          display: block;
          @apply --paper-font-common-base;
        }

        paper-input {
          width: 30px;
          text-align: center;
          --paper-input-container-input: {
            /* Damn you firefox
             * Needed to hide spin num in firefox
             * http://stackoverflow.com/questions/3790935/can-i-hide-the-html5-number-input-s-spin-box
             */
            -moz-appearance: textfield;
            @apply --paper-time-input-cotnainer;
          }
          ;
          --paper-input-container-input-webkit-spinner: {
            -webkit-appearance: none;
            margin: 0;
            display: none;
          }
          ;
        }

        paper-dropdown-menu {
          width: 55px;
          padding: 0;
          /* Force ripple to use the whole container */
          --paper-dropdown-menu-ripple: {
            color: var(--paper-time-input-dropdown-ripple-color, var(--primary-color));
          };
          --paper-input-container-input: {
            @apply --paper-font-button;
            text-align: center;
            padding-left: 5px;
            @apply --paper-time-dropdown-input-cotnainer;
          };
          --paper-input-container-underline: {
            border-color: transparent;
          }
          --paper-input-container-underline-focus: {
            border-color: transparent;
          };
        }

        paper-item {
          cursor: pointer;
          text-align: center;
          font-size: 14px;
        }

        paper-listbox {
          padding: 0;
        }

        label {
          @apply --paper-font-caption;
        }

        .time-input-wrap {
          @apply --layout-horizontal;
          @apply --layout-no-wrap;
        }

        [hidden] {
          display: none !important;
        }
      </style>

      <label hidden$="[[hideLabel]]">[[label]]</label>
      <div class="time-input-wrap">

        <!-- Hour Input -->
        <paper-input id="hour" type="number" value="{{hour}}" on-change="_shouldFormatHour" required="" auto-validate="[[autoValidate]]"
          prevent-invalid-input="" maxlength="2" max="[[_computeHourMax(format)]]" min="0" no-label-float="" disabled="[[disabled]]">
          <span suffix="" slot="suffix">:</span>
        </paper-input>

        <!-- Min Input -->
        <paper-input id="min" type="number" value="{{min}}" on-change="_formatMin" required="" auto-validate="[[autoValidate]]" prevent-invalid-input=""
          maxlength="2" max="59" min="0" no-label-float="" disabled="[[disabled]]">
        </paper-input>

        <!-- Dropdown Menu -->
        <paper-dropdown-menu id="dropdown" required="" hidden$="[[_equal(format, 24)]]" no-label-float="" disabled="[[disabled]]">

          <paper-listbox attr-for-selected="name" selected="{{amPm}}" slot="dropdown-content">
            <paper-item name="AM">AM</paper-item>
            <paper-item name="PM">PM</paper-item>
          </paper-listbox>
        </paper-dropdown-menu>

      </div>
    `}static get properties(){return{label:{type:String,value:"Time"},autoValidate:{type:Boolean,value:!0},hideLabel:{type:Boolean,value:!1},format:{type:Number,value:12},disabled:{type:Boolean,value:!1},hour:{type:String,notify:!0},min:{type:String,notify:!0},amPm:{type:String,notify:!0,value:"AM"},value:{type:String,notify:!0,readOnly:!0,computed:"_computeTime(min, hour, amPm)"}}}validate(){var e=!0;return!this.$.hour.validate()|!this.$.min.validate()&&(e=!1),12!==this.format||this.$.dropdown.validate()||(e=!1),e}_computeTime(e,t,a){if(t&&e)return 24===this.format&&(a=""),t+":"+e+" "+a}_formatMin(){1===this.min.toString().length&&(this.min=this.min<10?"0"+this.min:this.min)}_shouldFormatHour(){24===this.format&&1===this.hour.toString().length&&(this.hour=this.hour<10?"0"+this.hour:this.hour)}_computeHourMax(e){return 12===e?e:23}_equal(e,t){return e===t}}),customElements.define("more-info-input_datetime",class extends s.a{static get template(){return i["a"]`
    <div class$="[[computeClassNames(stateObj)]]">
      <template is="dom-if" if="[[doesHaveDate(stateObj)]]" restamp="">
        <div>
          <vaadin-date-picker id="dateInput" on-value-changed="dateTimeChanged" label="Date" value="{{selectedDate}}"></vaadin-date-picker>
        </div>
      </template>
      <template is="dom-if" if="[[doesHaveTime(stateObj)]]" restamp="">
        <div>
          <paper-time-input hour="{{selectedHour}}" min="{{selectedMinute}}" format="24"></paper-time-input>
        </div>
      </template>
    </div>
`}constructor(){super(),this.is_ready=!1}static get properties(){return{hass:{type:Object},stateObj:{type:Object,observer:"stateObjChanged"},selectedDate:{type:String,observer:"dateTimeChanged"},selectedHour:{type:Number,observer:"dateTimeChanged"},selectedMinute:{type:Number,observer:"dateTimeChanged"}}}ready(){super.ready(),this.is_ready=!0}getDateString(e){return"unknown"===e.state?"":(t=e.attributes.month<10?"0":"",a=e.attributes.day<10?"0":"",e.attributes.year+"-"+t+e.attributes.month+"-"+a+e.attributes.day);var t,a}dateTimeChanged(){if(!this.is_ready)return;let e,t=!1;const a={entity_id:this.stateObj.entity_id};if(this.stateObj.attributes.has_time){t|=parseInt(this.selectedMinute)!==this.stateObj.attributes.minute,t|=parseInt(this.selectedHour)!==this.stateObj.attributes.hour,e=this.selectedMinute<10?"0":"";var i=this.selectedHour+":"+e+this.selectedMinute;a.time=i}if(this.stateObj.attributes.has_date){if(0===this.selectedDate.length)return;const e=new Date(this.selectedDate);t|=new Date(this.stateObj.attributes.year,this.stateObj.attributes.month-1,this.stateObj.attributes.day)!==e,a.date=this.selectedDate}t&&this.hass.callService("input_datetime","set_datetime",a)}stateObjChanged(e){this.is_ready=!1,e.attributes.has_time&&(this.selectedHour=e.attributes.hour,this.selectedMinute=e.attributes.minute),e.attributes.has_date&&(this.selectedDate=this.getDateString(e)),this.is_ready=!0}doesHaveDate(e){return e.attributes.has_date}doesHaveTime(e){return e.attributes.has_time}computeClassNames(e){return"more-info-input_datetime "+Object(p.a)(e,["has_time","has_date"])}}),customElements.define("ha-color-picker",class extends(Object(r.a)(s.a)){static get template(){return i["a"]`
    <style>
      :host {
        user-select: none;
        -webkit-user-select: none;
      }

      #canvas {
        position: relative;
        width: 100%;
        max-width: 330px;
      }
      #canvas > * {
        display: block;
      }
      #interactionLayer {
        color: white;
        position: absolute;
        cursor: crosshair;
        width: 100%;
        height: 100%;
        overflow: visible;
      }
      #backgroundLayer {
        width: 100%;
        overflow: visible;
        --wheel-bordercolor: var(--ha-color-picker-wheel-bordercolor, white);
        --wheel-borderwidth: var(--ha-color-picker-wheel-borderwidth, 3);
        --wheel-shadow: var(--ha-color-picker-wheel-shadow, rgb(15, 15, 15) 10px 5px 5px 0px);
      }

      #marker {
        fill: currentColor;
        stroke: var(--ha-color-picker-marker-bordercolor, white);
        stroke-width: var(--ha-color-picker-marker-borderwidth, 3);
        filter: url(#marker-shadow)
      }
      .dragging #marker {
      }

      #colorTooltip {
        display: none;
        fill: currentColor;
        stroke: var(--ha-color-picker-tooltip-bordercolor, white);
        stroke-width: var(--ha-color-picker-tooltip-borderwidth, 3);
      }

      .touch.dragging #colorTooltip {
        display: inherit;
      }

    </style>
    <div id="canvas">
      <svg id="interactionLayer">
        <defs>
          <filter id="marker-shadow" x="-50%" y="-50%" width="200%" height="200%" filterUnits="objectBoundingBox">
             <feOffset result="offOut" in="SourceAlpha" dx="2" dy="2"></feOffset>
             <feGaussianBlur result="blurOut" in="offOut" stdDeviation="2"></feGaussianBlur>
             <feComponentTransfer in="blurOut" result="alphaOut">
               <feFuncA type="linear" slope="0.3"></feFuncA>
             </feComponentTransfer>
             <feBlend in="SourceGraphic" in2="alphaOut" mode="normal"></feBlend>
          </filter>
        </defs>
      </svg>
      <canvas id="backgroundLayer"></canvas>
    </div>
`}static get properties(){return{hsColor:{type:Object},desiredHsColor:{type:Object,observer:"applyHsColor"},width:{type:Number,value:500},height:{type:Number,value:500},radius:{type:Number,value:225},hueSegments:{type:Number,value:0},saturationSegments:{type:Number,value:0},ignoreSegments:{type:Boolean,value:!1},throttle:{type:Number,value:500}}}ready(){super.ready(),this.setupLayers(),this.drawColorWheel(),this.drawMarker(),this.interactionLayer.addEventListener("mousedown",e=>this.onMouseDown(e)),this.interactionLayer.addEventListener("touchstart",e=>this.onTouchStart(e))}convertToCanvasCoordinates(e,t){var a=this.interactionLayer.createSVGPoint();a.x=e,a.y=t;var i=a.matrixTransform(this.interactionLayer.getScreenCTM().inverse());return{x:i.x,y:i.y}}onMouseDown(e){const t=this.convertToCanvasCoordinates(e.clientX,e.clientY);this.isInWheel(t.x,t.y)&&(this.onMouseSelect(e),this.canvas.classList.add("mouse","dragging"),this.addEventListener("mousemove",this.onMouseSelect),this.addEventListener("mouseup",this.onMouseUp))}onMouseUp(){this.canvas.classList.remove("mouse","dragging"),this.removeEventListener("mousemove",this.onMouseSelect)}onMouseSelect(e){requestAnimationFrame(()=>this.processUserSelect(e))}onTouchStart(e){var t=e.changedTouches[0];const a=this.convertToCanvasCoordinates(t.clientX,t.clientY);if(this.isInWheel(a.x,a.y)){if(e.target===this.marker)return e.preventDefault(),this.canvas.classList.add("touch","dragging"),this.addEventListener("touchmove",this.onTouchSelect),void this.addEventListener("touchend",this.onTouchEnd);this.tapBecameScroll=!1,this.addEventListener("touchend",this.onTap),this.addEventListener("touchmove",()=>{this.tapBecameScroll=!0},{passive:!0})}}onTap(e){this.tapBecameScroll||(e.preventDefault(),this.onTouchSelect(e))}onTouchEnd(){this.canvas.classList.remove("touch","dragging"),this.removeEventListener("touchmove",this.onTouchSelect)}onTouchSelect(e){requestAnimationFrame(()=>this.processUserSelect(e.changedTouches[0]))}processUserSelect(e){var t=this.convertToCanvasCoordinates(e.clientX,e.clientY),a=this.getColor(t.x,t.y);this.onColorSelect(a)}onColorSelect(e){if(this.setMarkerOnColor(e),this.ignoreSegments||(e=this.applySegmentFilter(e)),this.applyColorToCanvas(e),this.colorSelectIsThrottled)return clearTimeout(this.ensureFinalSelect),void(this.ensureFinalSelect=setTimeout(()=>{this.fireColorSelected(e)},this.throttle));this.fireColorSelected(e),this.colorSelectIsThrottled=!0,setTimeout(()=>{this.colorSelectIsThrottled=!1},this.throttle)}fireColorSelected(e){this.hsColor=e,this.fire("colorselected",{hs:{h:e.h,s:e.s}})}setMarkerOnColor(e){var t=e.s*this.radius,a=(e.h-180)/180*Math.PI,i=`translate(${-t*Math.cos(a)},${-t*Math.sin(a)})`;this.marker.setAttribute("transform",i),this.tooltip.setAttribute("transform",i)}applyColorToCanvas(e){this.interactionLayer.style.color=`hsl(${e.h}, 100%, ${100-50*e.s}%)`}applyHsColor(e){this.hsColor&&this.hsColor.h===e.h&&this.hsColor.s===e.s||(this.setMarkerOnColor(e),this.ignoreSegments||(e=this.applySegmentFilter(e)),this.hsColor=e,this.applyColorToCanvas(e))}getAngle(e,t){return Math.atan2(-t,-e)/Math.PI*180+180}isInWheel(e,t){return this.getDistance(e,t)<=1}getDistance(e,t){return Math.sqrt(e*e+t*t)/this.radius}getColor(e,t){var a=this.getAngle(e,t),i=this.getDistance(e,t);return{h:a,s:Math.min(i,1)}}applySegmentFilter(e){if(this.hueSegments){const t=360/this.hueSegments,a=t/2;e.h-=a,e.h<0&&(e.h+=360);const i=e.h%t;e.h-=i-t}if(this.saturationSegments)if(1===this.saturationSegments)e.s=1;else{var t=1/this.saturationSegments,a=1/(this.saturationSegments-1),i=Math.floor(e.s/t)*a;e.s=Math.min(i,1)}return e}setupLayers(){this.canvas=this.$.canvas,this.backgroundLayer=this.$.backgroundLayer,this.interactionLayer=this.$.interactionLayer,this.originX=this.width/2,this.originY=this.originX,this.backgroundLayer.width=this.width,this.backgroundLayer.height=this.height,this.interactionLayer.setAttribute("viewBox",`${-this.originX} ${-this.originY} ${this.width} ${this.height}`)}drawColorWheel(){let e,t,a,i;const s=this.backgroundLayer.getContext("2d"),r=this.originX,o=this.originY,n=this.radius,l=window.getComputedStyle(this.backgroundLayer,null),d=parseInt(l.getPropertyValue("--wheel-borderwidth"),10),p=l.getPropertyValue("--wheel-bordercolor").trim(),c=l.getPropertyValue("--wheel-shadow").trim();if("none"!==c){const s=c.split("px ");e=s.pop(),t=parseInt(s[0],10),a=parseInt(s[1],10),i=parseInt(s[2],10)||0}const u=n+d/2,h=n,m=n+d;"none"!==l.shadow&&(s.save(),s.beginPath(),s.arc(r,o,m,0,2*Math.PI,!1),s.shadowColor=e,s.shadowOffsetX=t,s.shadowOffsetY=a,s.shadowBlur=i,s.fillStyle="white",s.fill(),s.restore()),function(e,t){const a=360/(e=e||360),i=a/2;for(var n=0;n<=360;n+=a){var l=(n-i)*(Math.PI/180),d=(n+i+1)*(Math.PI/180);s.beginPath(),s.moveTo(r,o),s.arc(r,o,h,l,d,!1),s.closePath();var p=s.createRadialGradient(r,o,0,r,o,h);let e=100;if(p.addColorStop(0,`hsl(${n}, 100%, ${e}%)`),t>0){const a=1/t;let i=0;for(var c=1;c<t;c+=1){var u=e;e=100-50*(i=c*a),p.addColorStop(i,`hsl(${n}, 100%, ${u}%)`),p.addColorStop(i,`hsl(${n}, 100%, ${e}%)`)}p.addColorStop(i,`hsl(${n}, 100%, 50%)`)}p.addColorStop(1,`hsl(${n}, 100%, 50%)`),s.fillStyle=p,s.fill()}}(this.hueSegments,this.saturationSegments),d>0&&(s.beginPath(),s.arc(r,o,u,0,2*Math.PI,!1),s.lineWidth=d,s.strokeStyle=p,s.stroke())}drawMarker(){const e=this.interactionLayer,t=.08*this.radius,a=.15*this.radius,i=-3*a;e.marker=document.createElementNS("http://www.w3.org/2000/svg","circle"),e.marker.setAttribute("id","marker"),e.marker.setAttribute("r",t),this.marker=e.marker,e.appendChild(e.marker),e.tooltip=document.createElementNS("http://www.w3.org/2000/svg","circle"),e.tooltip.setAttribute("id","colorTooltip"),e.tooltip.setAttribute("r",a),e.tooltip.setAttribute("cx",0),e.tooltip.setAttribute("cy",i),this.tooltip=e.tooltip,e.appendChild(e.tooltip)}});const f={1:"has-brightness",2:"has-color_temp",4:"has-effect_list",16:"has-color",128:"has-white_value"};customElements.define("more-info-light",class extends(Object(o.a)(Object(r.a)(s.a))){static get template(){return i["a"]`
  <style include="iron-flex"></style>
  <style>
    .effect_list {
      padding-bottom: 16px;
    }

    .effect_list, .brightness, .color_temp, .white_value {
      max-height: 0px;
      overflow: hidden;
      transition: max-height .5s ease-in;
    }

    .color_temp {
      --ha-slider-background: -webkit-linear-gradient(right, rgb(255, 160, 0) 0%, white 50%, rgb(166, 209, 255) 100%);
      /* The color temp minimum value shouldn't be rendered differently. It's not "off". */
      --paper-slider-knob-start-border-color: var(--primary-color);
    }

    ha-color-picker {
      display: block;
      width: 100%;

      max-height: 0px;
      overflow: hidden;
      transition: max-height .5s ease-in;
    }

    .has-effect_list.is-on .effect_list,
    .has-brightness .brightness,
    .has-color_temp.is-on .color_temp,
    .has-white_value.is-on .white_value {
      max-height: 84px;
    }

    .has-color.is-on ha-color-picker {
      max-height: 500px;
      overflow: visible;
      --ha-color-picker-wheel-borderwidth: 5;
      --ha-color-picker-wheel-bordercolor: white;
      --ha-color-picker-wheel-shadow: none;
      --ha-color-picker-marker-borderwidth: 2;
      --ha-color-picker-marker-bordercolor: white;
    }

    .is-unavailable .control {
      max-height: 0px;
    }

    paper-item {
      cursor: pointer;
    }
  </style>

  <div class$="[[computeClassNames(stateObj)]]">

    <div class="control brightness">
      <ha-labeled-slider caption="[[localize('ui.card.light.brightness')]]" icon="hass:brightness-5" max="255" value="{{brightnessSliderValue}}" on-change="brightnessSliderChanged"></ha-labeled-slider>
    </div>

    <div class="control color_temp">
      <ha-labeled-slider caption="[[localize('ui.card.light.color_temperature')]]" icon="hass:thermometer" min="[[stateObj.attributes.min_mireds]]" max="[[stateObj.attributes.max_mireds]]" value="{{ctSliderValue}}" on-change="ctSliderChanged"></ha-labeled-slider>
    </div>

    <div class="control white_value">
      <ha-labeled-slider caption="[[localize('ui.card.light.white_value')]]" icon="hass:file-word-box" max="255" value="{{wvSliderValue}}" on-change="wvSliderChanged"></ha-labeled-slider>
    </div>

    <ha-color-picker class="control color" on-colorselected="colorPicked" desired-hs-color="{{colorPickerColor}}" throttle="500" hue-segments="24" saturation-segments="8">
    </ha-color-picker>

    <div class="control effect_list">
      <paper-dropdown-menu label-float="" dynamic-align="" label="[[localize('ui.card.light.effect')]]">
        <paper-listbox slot="dropdown-content" selected="{{effectIndex}}">
          <template is="dom-repeat" items="[[stateObj.attributes.effect_list]]">
            <paper-item>[[item]]</paper-item>
          </template>
        </paper-listbox>
      </paper-dropdown-menu>
    </div>

    <ha-attributes state-obj="[[stateObj]]" extra-filters="brightness,color_temp,white_value,effect_list,effect,hs_color,rgb_color,xy_color,min_mireds,max_mireds"></ha-attributes>
  </div>
`}static get properties(){return{hass:{type:Object},stateObj:{type:Object,observer:"stateObjChanged"},effectIndex:{type:Number,value:-1,observer:"effectChanged"},brightnessSliderValue:{type:Number,value:0},ctSliderValue:{type:Number,value:0},wvSliderValue:{type:Number,value:0},colorPickerColor:{type:Object}}}stateObjChanged(e,t){const a={brightnessSliderValue:0};e&&"on"===e.state&&(a.brightnessSliderValue=e.attributes.brightness,a.ctSliderValue=e.attributes.color_temp,a.wvSliderValue=e.attributes.white_value,e.attributes.hs_color&&(a.colorPickerColor={h:e.attributes.hs_color[0],s:e.attributes.hs_color[1]/100}),e.attributes.effect_list?a.effectIndex=e.attributes.effect_list.indexOf(e.attributes.effect):a.effectIndex=-1),this.setProperties(a),t&&setTimeout(()=>{this.fire("iron-resize")},500)}computeClassNames(e){const t=[c(e,f)];return e&&"on"===e.state&&t.push("is-on"),e&&"unavailable"===e.state&&t.push("is-unavailable"),t.join(" ")}effectChanged(e){var t;""!==e&&-1!==e&&(t=this.stateObj.attributes.effect_list[e])!==this.stateObj.attributes.effect&&this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,effect:t})}brightnessSliderChanged(e){var t=parseInt(e.target.value,10);isNaN(t)||(0===t?this.hass.callService("light","turn_off",{entity_id:this.stateObj.entity_id}):this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,brightness:t}))}ctSliderChanged(e){var t=parseInt(e.target.value,10);isNaN(t)||this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,color_temp:t})}wvSliderChanged(e){var t=parseInt(e.target.value,10);isNaN(t)||this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,white_value:t})}serviceChangeColor(e,t,a){e.callService("light","turn_on",{entity_id:t,hs_color:[a.h,100*a.s]})}colorPicked(e){this.serviceChangeColor(this.hass,this.stateObj.entity_id,e.detail.hs)}}),customElements.define("more-info-lock",class extends(Object(o.a)(s.a)){static get template(){return i["a"]`
      <style>
        paper-input {
          display: inline-block;
        }
      </style>

      <template is="dom-if" if="[[stateObj.attributes.code_format]]">
        <paper-input label="[[localize('ui.card.lock.code')]]" value="{{enteredCode}}" pattern="[[stateObj.attributes.code_format]]" type="password"></paper-input>
        <paper-button on-click="callService" data-service="unlock" hidden$="[[!isLocked]]">[[localize('ui.card.lock.unlock')]]</paper-button>
        <paper-button on-click="callService" data-service="lock" hidden$="[[isLocked]]">[[localize('ui.card.lock.lock')]]</paper-button>
      </template>
      <ha-attributes state-obj="[[stateObj]]" extra-filters="code_format"></ha-attributes>
    `}static get properties(){return{hass:Object,stateObj:{type:Object,observer:"stateObjChanged"},enteredCode:{type:String,value:""},isLocked:Boolean}}stateObjChanged(e){e&&(this.isLocked="locked"===e.state)}callService(e){const t=e.target.getAttribute("data-service"),a={entity_id:this.stateObj.entity_id,code:this.enteredCode};this.hass.callService("lock",t,a)}}),a(62);var _=a(99),O=a(127);customElements.define("more-info-media_player",class extends(Object(o.a)(Object(r.a)(s.a))){static get template(){return i["a"]`
  <style include="iron-flex iron-flex-alignment"></style>
  <style>
    .media-state {
      text-transform: capitalize;
    }

    paper-icon-button[highlight] {
      color: var(--accent-color);
    }

    .volume {
      margin-bottom: 8px;

      max-height: 0px;
      overflow: hidden;
      transition: max-height .5s ease-in;
    }

    .has-volume_level .volume {
      max-height: 40px;
    }

    iron-icon.source-input {
      padding: 7px;
      margin-top: 15px;
    }

    paper-dropdown-menu.source-input {
      margin-left: 10px;
    }

    [hidden] {
      display: none !important;
    }

    paper-item {
      cursor: pointer;
    }
  </style>

  <div class$="[[computeClassNames(stateObj)]]">
    <div class="layout horizontal">
      <div class="flex">
        <paper-icon-button icon="hass:power" highlight$="[[playerObj.isOff]]" on-click="handleTogglePower" hidden$="[[computeHidePowerButton(playerObj)]]"></paper-icon-button>
      </div>
      <div>
        <template is="dom-if" if="[[computeShowPlaybackControls(playerObj)]]">
          <paper-icon-button icon="hass:skip-previous" on-click="handlePrevious" hidden$="[[!playerObj.supportsPreviousTrack]]"></paper-icon-button>
          <paper-icon-button icon="[[computePlaybackControlIcon(playerObj)]]" on-click="handlePlaybackControl" hidden$="[[!computePlaybackControlIcon(playerObj)]]" highlight=""></paper-icon-button>
          <paper-icon-button icon="hass:skip-next" on-click="handleNext" hidden$="[[!playerObj.supportsNextTrack]]"></paper-icon-button>
        </template>
      </div>
    </div>
    <!-- VOLUME -->
    <div class="volume_buttons center horizontal layout" hidden$="[[computeHideVolumeButtons(playerObj)]]">
      <paper-icon-button on-click="handleVolumeTap" icon="hass:volume-off"></paper-icon-button>
      <paper-icon-button id="volumeDown" disabled$="[[playerObj.isMuted]]" on-mousedown="handleVolumeDown" on-touchstart="handleVolumeDown" icon="hass:volume-medium"></paper-icon-button>
      <paper-icon-button id="volumeUp" disabled$="[[playerObj.isMuted]]" on-mousedown="handleVolumeUp" on-touchstart="handleVolumeUp" icon="hass:volume-high"></paper-icon-button>
    </div>
    <div class="volume center horizontal layout" hidden$="[[!playerObj.supportsVolumeSet]]">
      <paper-icon-button on-click="handleVolumeTap" hidden$="[[playerObj.supportsVolumeButtons]]" icon="[[computeMuteVolumeIcon(playerObj)]]"></paper-icon-button>
      <ha-paper-slider disabled$="[[playerObj.isMuted]]" min="0" max="100" value="[[playerObj.volumeSliderValue]]" on-change="volumeSliderChanged" class="flex" ignore-bar-touch="">
      </ha-paper-slider>
    </div>
    <!-- SOURCE PICKER -->
    <div class="controls layout horizontal justified" hidden$="[[computeHideSelectSource(playerObj)]]">
      <iron-icon class="source-input" icon="hass:login-variant"></iron-icon>
      <paper-dropdown-menu class="flex source-input" dynamic-align="" label-float="" label="[[localize('ui.card.media_player.source')]]">
        <paper-listbox slot="dropdown-content" selected="{{sourceIndex}}">
          <template is="dom-repeat" items="[[playerObj.sourceList]]">
            <paper-item>[[item]]</paper-item>
          </template>
        </paper-listbox>
      </paper-dropdown-menu>
    </div>
    <!-- SOUND MODE PICKER -->
    <template is='dom-if' if='[[!computeHideSelectSoundMode(playerObj)]]'>
      <div class="controls layout horizontal justified">
        <iron-icon class="source-input" icon="hass:music-note"></iron-icon>
        <paper-dropdown-menu class="flex source-input" dynamic-align label-float label="[[localize('ui.card.media_player.sound_mode')]]">
          <paper-listbox slot="dropdown-content" attr-for-selected="item-name" selected="{{SoundModeInput}}">
            <template is='dom-repeat' items='[[playerObj.soundModeList]]'>
              <paper-item item-name$="[[item]]">[[item]]</paper-item>
            </template>
          </paper-listbox>
        </paper-dropdown-menu>
      </div>
    </template>
    <!-- TTS -->
    <div hidden$="[[computeHideTTS(ttsLoaded, playerObj)]]" class="layout horizontal end">
      <paper-input id="ttsInput" label="[[localize('ui.card.media_player.text_to_speak')]]" class="flex" value="{{ttsMessage}}" on-keydown="ttsCheckForEnter"></paper-input>
      <paper-icon-button icon="hass:send" on-click="sendTTS"></paper-icon-button>
    </div>
  </div>
`}static get properties(){return{hass:Object,stateObj:Object,playerObj:{type:Object,computed:"computePlayerObj(hass, stateObj)",observer:"playerObjChanged"},sourceIndex:{type:Number,value:0,observer:"handleSourceChanged"},SoundModeInput:{type:String,value:"",observer:"handleSoundModeChanged"},ttsLoaded:{type:Boolean,computed:"computeTTSLoaded(hass)"},ttsMessage:{type:String,value:""}}}computePlayerObj(e,t){return new _.a(e,t)}playerObjChanged(e,t){e&&void 0!==e.sourceList&&(this.sourceIndex=e.sourceList.indexOf(e.source)),e&&void 0!==e.soundModeList&&(this.SoundModeInput=e.soundMode),t&&setTimeout(()=>{this.fire("iron-resize")},500)}computeClassNames(e){return Object(p.a)(e,["volume_level"])}computeMuteVolumeIcon(e){return e.isMuted?"hass:volume-off":"hass:volume-high"}computeHideVolumeButtons(e){return!e.supportsVolumeButtons||e.isOff}computeShowPlaybackControls(e){return!e.isOff&&e.hasMediaControl}computePlaybackControlIcon(e){return e.isPlaying?e.supportsPause?"hass:pause":"hass:stop":e.supportsPlay?"hass:play":null}computeHidePowerButton(e){return e.isOff?!e.supportsTurnOn:!e.supportsTurnOff}computeHideSelectSource(e){return e.isOff||!e.supportsSelectSource||!e.sourceList}computeHideSelectSoundMode(e){return e.isOff||!e.supportsSelectSoundMode||!e.soundModeList}computeHideTTS(e,t){return!e||!t.supportsPlayMedia}computeTTSLoaded(e){return Object(O.a)(e,"tts")}handleTogglePower(){this.playerObj.togglePower()}handlePrevious(){this.playerObj.previousTrack()}handlePlaybackControl(){this.playerObj.mediaPlayPause()}handleNext(){this.playerObj.nextTrack()}handleSourceChanged(e,t){if(!this.playerObj||!this.playerObj.supportsSelectSource||void 0===this.playerObj.sourceList||e<0||e>=this.playerObj.sourceList||void 0===t)return;const a=this.playerObj.sourceList[e];a!==this.playerObj.source&&this.playerObj.selectSource(a)}handleSoundModeChanged(e,t){t&&e!==this.playerObj.soundMode&&this.playerObj.supportsSelectSoundMode&&this.playerObj.selectSoundMode(e)}handleVolumeTap(){this.playerObj.supportsVolumeMute&&this.playerObj.volumeMute(!this.playerObj.isMuted)}handleVolumeUp(){const e=this.$.volumeUp;this.handleVolumeWorker("volume_up",e,!0)}handleVolumeDown(){const e=this.$.volumeDown;this.handleVolumeWorker("volume_down",e,!0)}handleVolumeWorker(e,t,a){(a||void 0!==t&&t.pointerDown)&&(this.playerObj.callService(e),setTimeout(()=>this.handleVolumeWorker(e,t,!1),500))}volumeSliderChanged(e){const t=parseFloat(e.target.value),a=t>0?t/100:0;this.playerObj.setVolume(a)}ttsCheckForEnter(e){13===e.keyCode&&this.sendTTS()}sendTTS(){const e=this.hass.config.services.tts,t=Object.keys(e).sort();let a,i;for(i=0;i<t.length;i++)if(-1!==t[i].indexOf("_say")){a=t[i];break}a&&(this.hass.callService("tts",a,{entity_id:this.stateObj.entity_id,message:this.ttsMessage}),this.ttsMessage="",this.$.ttsInput.focus())}}),customElements.define("more-info-script",class extends s.a{static get template(){return i["a"]`
    <style include="iron-flex iron-flex-alignment"></style>

    <div class="layout vertical">
      <div class="data-entry layout justified horizontal">
        <div class="key">Last Action</div>
        <div class="value">[[stateObj.attributes.last_action]]</div>
      </div>
    </div>
`}static get properties(){return{stateObj:{type:Object}}}});var j=a(94);customElements.define("more-info-sun",class extends s.a{static get template(){return i["a"]`
    <style include="iron-flex iron-flex-alignment"></style>

    <template is="dom-repeat" items="[[computeOrder(risingDate, settingDate)]]">
      <div class="data-entry layout justified horizontal">
        <div class="key">
          <span>[[itemCaption(item)]]</span>
          <ha-relative-time hass="[[hass]]" datetime-obj="[[itemDate(item)]]"></ha-relative-time>
        </div>
        <div class="value">[[itemValue(item)]]</div>
      </div>
    </template>
      <div class="data-entry layout justified horizontal">
        <div class="key">Elevation</div>
        <div class="value">[[stateObj.attributes.elevation]]</div>
     </div>
`}static get properties(){return{hass:Object,stateObj:Object,risingDate:{type:Object,computed:"computeRising(stateObj)"},settingDate:{type:Object,computed:"computeSetting(stateObj)"}}}computeRising(e){return new Date(e.attributes.next_rising)}computeSetting(e){return new Date(e.attributes.next_setting)}computeOrder(e,t){return e>t?["set","ris"]:["ris","set"]}itemCaption(e){return"ris"===e?"Rising ":"Setting "}itemDate(e){return"ris"===e?this.risingDate:this.settingDate}itemValue(e){return Object(j.a)(this.itemDate(e))}}),customElements.define("more-info-updater",class extends s.a{static get template(){return i["a"]`
    <style>
      .link {
        color: #03A9F4;
      }
    </style>

    <div>
      <a class="link" href="https://www.home-assistant.io/docs/installation/updating/" target="_blank">Update Instructions</a>
    </div>
`}static get properties(){return{stateObj:{type:Object}}}computeReleaseNotes(e){return e.attributes.release_notes||"https://www.home-assistant.io/docs/installation/updating/"}}),customElements.define("more-info-vacuum",class extends s.a{static get template(){return i["a"]`
    <style include="iron-flex iron-flex-alignment"></style>
    <style>
      :host {
        @apply --paper-font-body1;
        line-height: 1.5;
      }

      .status-subtitle {
        color: var(--secondary-text-color);
      }

      paper-item {
        cursor: pointer;
      }

    </style>

    <div class="horizontal justified layout">
      <div hidden$="[[!supportsStatus(stateObj)]]">
        <span class="status-subtitle">Status: </span><span><strong>[[stateObj.attributes.status]]</strong></span>
      </div>
      <div hidden$="[[!supportsBattery(stateObj)]]">
        <span><iron-icon icon="[[stateObj.attributes.battery_icon]]"></iron-icon> [[stateObj.attributes.battery_level]] %</span>
      </div>
    </div>
    <div hidden$="[[!supportsCommandBar(stateObj)]]">
      <p></p>
      <div class="status-subtitle">Vacuum cleaner commands:</div>
      <div class="horizontal justified layout">
        <div hidden$="[[!supportsPause(stateObj)]]">
          <paper-icon-button icon="hass:play-pause" on-click="onPlayPause" title="Start/Pause"></paper-icon-button>
        </div>
        <div hidden$="[[!supportsStop(stateObj)]]">
          <paper-icon-button icon="hass:stop" on-click="onStop" title="Stop"></paper-icon-button>
        </div>
        <div hidden$="[[!supportsCleanSpot(stateObj)]]">
        <paper-icon-button icon="hass:broom" on-click="onCleanSpot" title="Clean spot"></paper-icon-button>
        </div>
        <div hidden$="[[!supportsLocate(stateObj)]]">
        <paper-icon-button icon="hass:map-marker" on-click="onLocate" title="Locate"></paper-icon-button>
        </div>
        <div hidden$="[[!supportsReturnHome(stateObj)]]">
        <paper-icon-button icon="hass:home-map-marker" on-click="onReturnHome" title="Return home"></paper-icon-button>
        </div>
      </div>
    </div>

    <div hidden$="[[!supportsFanSpeed(stateObj)]]">
      <div class="horizontal justified layout">
        <paper-dropdown-menu label-float="" dynamic-align="" label="Fan speed">
          <paper-listbox slot="dropdown-content" selected="{{fanSpeedIndex}}">
            <template is="dom-repeat" items="[[stateObj.attributes.fan_speed_list]]">
              <paper-item>[[item]]</paper-item>
            </template>
          </paper-listbox>
        </paper-dropdown-menu>
        <div style="justify-content: center; align-self: center; padding-top: 1.3em">
          <span><iron-icon icon="hass:fan"></iron-icon> [[stateObj.attributes.fan_speed]]</span>
        </div>
      </div>
      <p></p>
    </div>
    <ha-attributes state-obj="[[stateObj]]" extra-filters="fan_speed,fan_speed_list,status,battery_level,battery_icon"></ha-attributes>
`}static get properties(){return{hass:{type:Object},inDialog:{type:Boolean,value:!1},stateObj:{type:Object},fanSpeedIndex:{type:Number,value:-1,observer:"fanSpeedChanged"}}}supportsPause(e){return 0!=(4&e.attributes.supported_features)}supportsStop(e){return 0!=(8&e.attributes.supported_features)}supportsReturnHome(e){return 0!=(16&e.attributes.supported_features)}supportsFanSpeed(e){return 0!=(32&e.attributes.supported_features)}supportsBattery(e){return 0!=(64&e.attributes.supported_features)}supportsStatus(e){return 0!=(128&e.attributes.supported_features)}supportsLocate(e){return 0!=(512&e.attributes.supported_features)}supportsCleanSpot(e){return 0!=(1024&e.attributes.supported_features)}supportsCommandBar(e){return 0!=(4&e.attributes.supported_features)|0!=(8&e.attributes.supported_features)|0!=(16&e.attributes.supported_features)|0!=(512&e.attributes.supported_features)|0!=(1024&e.attributes.supported_features)}fanSpeedChanged(e){var t;""!==e&&-1!==e&&(t=this.stateObj.attributes.fan_speed_list[e])!==this.stateObj.attributes.fan_speed&&this.hass.callService("vacuum","set_fan_speed",{entity_id:this.stateObj.entity_id,fan_speed:t})}onStop(){this.hass.callService("vacuum","stop",{entity_id:this.stateObj.entity_id})}onPlayPause(){this.hass.callService("vacuum","start_pause",{entity_id:this.stateObj.entity_id})}onLocate(){this.hass.callService("vacuum","locate",{entity_id:this.stateObj.entity_id})}onCleanSpot(){this.hass.callService("vacuum","clean_spot",{entity_id:this.stateObj.entity_id})}onReturnHome(){this.hass.callService("vacuum","return_to_base",{entity_id:this.stateObj.entity_id})}}),customElements.define("more-info-weather",class extends(Object(o.a)(s.a)){static get template(){return i["a"]`
    <style>
      iron-icon {
        color: var(--paper-item-icon-color);
      }
      .section {
        margin: 16px 0 8px 0;
        font-size: 1.2em;
      }

      .flex {
        display: flex;
        height: 32px;
        align-items: center;
      }

      .main {
        flex: 1;
        margin-left: 24px;
      }

      .temp,
      .templow {
        min-width: 48px;
        text-align: right;
      }

      .templow {
        margin: 0 16px;
        color: var(--secondary-text-color);
      }

      .attribution {
        color: var(--secondary-text-color);
        text-align: center;
      }
    </style>

    <div class="flex">
      <iron-icon icon="hass:thermometer"></iron-icon>
      <div class="main">[[localize('ui.card.weather.attributes.temperature')]]</div>
      <div>[[stateObj.attributes.temperature]] [[getUnit('temperature')]]</div>
    </div>
    <template is="dom-if" if="[[stateObj.attributes.pressure]]">
      <div class="flex">
        <iron-icon icon="hass:gauge"></iron-icon>
        <div class="main">[[localize('ui.card.weather.attributes.air_pressure')]]</div>
        <div>[[stateObj.attributes.pressure]] [[getUnit('air_pressure')]]</div>
      </div>
    </template>
    <template is="dom-if" if="[[stateObj.attributes.humidity]]">
      <div class="flex">
        <iron-icon icon="hass:water-percent"></iron-icon>
        <div class="main">[[localize('ui.card.weather.attributes.humidity')]]</div>
        <div>[[stateObj.attributes.humidity]] %</div>
      </div>
    </template>
    <template is="dom-if" if="[[stateObj.attributes.wind_speed]]">
      <div class="flex">
        <iron-icon icon="hass:weather-windy"></iron-icon>
        <div class="main">[[localize('ui.card.weather.attributes.wind_speed')]]</div>
        <div>[[getWind(stateObj.attributes.wind_speed, stateObj.attributes.wind_bearing, localize)]]</div>
      </div>
    </template>
    <template is="dom-if" if="[[stateObj.attributes.visibility]]">
      <div class="flex">
        <iron-icon icon="hass:eye"></iron-icon>
        <div class="main">[[localize('ui.card.weather.attributes.visibility')]]</div>
        <div>[[stateObj.attributes.visibility]] [[getUnit('length')]]</div>
      </div>
    </template>

    <template is="dom-if" if="[[stateObj.attributes.forecast]]">
      <div class="section">[[localize('ui.card.weather.forecast')]]:</div>
      <template is="dom-repeat" items="[[stateObj.attributes.forecast]]">
        <div class="flex">
          <template is="dom-if" if="[[item.condition]]">
            <iron-icon icon="[[getWeatherIcon(item.condition)]]"></iron-icon>
          </template>
          <div class="main">[[computeDateTime(item.datetime)]]</div>
          <template is="dom-if" if="[[item.templow]]">
            <div class="templow">[[item.templow]] [[getUnit('temperature')]]</div>
          </template>
          <div class="temp">[[item.temperature]] [[getUnit('temperature')]]</div>
        </div>
      </template>
    </template>

    <template is="dom-if" if="stateObj.attributes.attribution">
      <div class="attribution">[[stateObj.attributes.attribution]]</div>
    </template>
`}static get properties(){return{hass:Object,stateObj:Object}}constructor(){super(),this.cardinalDirections=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"],this.weatherIcons={"clear-night":"hass:weather-night",cloudy:"hass:weather-cloudy",fog:"hass:weather-fog",hail:"hass:weather-hail",lightning:"mid:weather-lightning","lightning-rainy":"hass:weather-lightning-rainy",partlycloudy:"hass:weather-partlycloudy",pouring:"hass:weather-pouring",rainy:"hass:weather-rainy",snowy:"hass:weather-snowy","snowy-rainy":"hass:weather-snowy-rainy",sunny:"hass:weather-sunny",windy:"hass:weather-windy","windy-variant":"hass:weather-windy-variant"}}computeDateTime(e){const t=new Date(e),a=this.stateObj.attributes.attribution;return"Powered by Dark Sky"===a||"Data provided by OpenWeatherMap"===a?(new Date).getDay()===t.getDay()?t.toLocaleTimeString(this.hass.selectedLanguage||this.hass.language,{hour:"numeric"}):t.toLocaleDateString(this.hass.selectedLanguage||this.hass.language,{weekday:"long",hour:"numeric"}):t.toLocaleDateString(this.hass.selectedLanguage||this.hass.language,{weekday:"long",month:"short",day:"numeric"})}getUnit(e){const t=this.hass.config.core.unit_system.length||"";switch(e){case"air_pressure":return"km"===t?"hPa":"inHg";case"length":return t;case"precipitation":return"km"===t?"mm":"in";default:return this.hass.config.core.unit_system[e]||""}}windBearingToText(e){const t=parseInt(e);return isFinite(t)?this.cardinalDirections[((t+11.25)/22.5|0)%16]:e}getWind(e,t,a){if(null!=t){const i=this.windBearingToText(t);return`${e} ${this.getUnit("length")}/h (${a(`ui.card.weather.cardinal_direction.${i.toLowerCase()}`)||i})`}return`${e} ${this.getUnit("length")}/h`}getWeatherIcon(e){return this.weatherIcons[e]}}),customElements.define("more-info-content",class extends s.a{static get properties(){return{hass:Object,stateObj:Object}}static get observers(){return["stateObjChanged(stateObj, hass)"]}constructor(){super(),this.style.display="block"}stateObjChanged(e,t){let a;e&&t?(this._detachedChild&&(this.appendChild(this._detachedChild),this._detachedChild=null),a=e.attributes&&"custom_ui_more_info"in e.attributes?e.attributes.custom_ui_more_info:"more-info-"+Object(y.a)(e),Object(v.a)(this,a.toUpperCase(),{hass:t,stateObj:e})):this.lastChild&&(this._detachedChild=this.lastChild,this.removeChild(this.lastChild))}});var x=a(33);const w=["camera","configurator","history_graph"];customElements.define("more-info-controls",class extends(Object(r.a)(s.a)){static get template(){return i["a"]`
  <style include="ha-style-dialog">
    app-toolbar {
      color: var(--more-info-header-color);
      background-color: var(--more-info-header-background);
    }

    app-toolbar [main-title] {
      @apply --ha-more-info-app-toolbar-title;
    }

    state-card-content {
      display: block;
      padding: 16px;
    }

    state-history-charts {
      max-width: 100%;
      margin-bottom: 16px;
    }

    @media all and (min-width: 451px) and (min-height: 501px) {
      .main-title {
        pointer-events: auto;
        cursor: default;
      }
    }

    :host([domain=camera]) paper-dialog-scrollable {
      margin: 0 -24px -5px;
    }
  </style>

  <app-toolbar>
    <paper-icon-button icon="hass:close" dialog-dismiss=""></paper-icon-button>
    <div class="main-title" main-title="" on-click="enlarge">[[_computeStateName(stateObj)]]</div>
    <template is="dom-if" if="[[canConfigure]]">
      <paper-icon-button icon="hass:settings" on-click="_gotoSettings"></paper-icon-button>
    </template>
  </app-toolbar>

  <template is="dom-if" if="[[_computeShowStateInfo(stateObj)]]" restamp="">
    <state-card-content state-obj="[[stateObj]]" hass="[[hass]]" in-dialog=""></state-card-content>
  </template>
  <paper-dialog-scrollable dialog-element="[[dialogElement]]">
    <template is="dom-if" if="[[_computeShowHistoryComponent(hass, stateObj)]]" restamp="">
      <ha-state-history-data hass="[[hass]]" filter-type="recent-entity" entity-id="[[stateObj.entity_id]]" data="{{_stateHistory}}" is-loading="{{_stateHistoryLoading}}" cache-config="[[_cacheConfig]]"></ha-state-history-data>
      <state-history-charts hass="[[hass]]" history-data="[[_stateHistory]]" is-loading-data="[[_stateHistoryLoading]]" up-to-now no-single="[[large]]"></state-history-charts>
    </template>
    <more-info-content state-obj="[[stateObj]]" hass="[[hass]]"></more-info-content>
  </paper-dialog-scrollable>
`}static get properties(){return{hass:Object,stateObj:{type:Object,observer:"_stateObjChanged"},dialogElement:Object,canConfigure:Boolean,domain:{type:String,reflectToAttribute:!0,computed:"_computeDomain(stateObj)"},_stateHistory:Object,_stateHistoryLoading:Boolean,large:{type:Boolean,value:!1,notify:!0},_cacheConfig:{type:Object,value:{refresh:60,cacheKey:null,hoursToShow:24}}}}enlarge(){this.large=!this.large}_computeShowStateInfo(e){return!e||!w.includes(Object(g.a)(e))}_computeShowHistoryComponent(e,t){return e&&t&&Object(O.a)(e,"history")&&!x.d.includes(Object(g.a)(t))}_computeDomain(e){return e?Object(g.a)(e):""}_computeStateName(e){return e?Object(n.a)(e):""}_stateObjChanged(e){e&&this._cacheConfig.cacheKey!==`more_info.${e.entity_id}`&&(this._cacheConfig=Object.assign({},this._cacheConfig,{cacheKey:`more_info.${e.entity_id}`}))}_gotoSettings(){this.fire("more-info-page",{page:"settings"})}}),customElements.define("more-info-settings",class extends(Object(o.a)(Object(r.a)(s.a))){static get template(){return i["a"]`
    <style>
      app-toolbar {
        color: var(--more-info-header-color);
        background-color: var(--more-info-header-background);

        /* to fit save button */
        padding-right: 0;
      }

      app-toolbar [main-title] {
        @apply --ha-more-info-app-toolbar-title;
      }

      app-toolbar paper-button {
        font-size: .8em;
        margin: 0;
      }

      .form {
        padding: 0 24px 24px;
      }
    </style>

    <app-toolbar>
      <paper-icon-button icon="hass:arrow-left" on-click="_backTapped"></paper-icon-button>
      <div main-title="">[[_computeStateName(stateObj)]]</div>
      <paper-button on-click="_save">[[localize('ui.dialogs.more_info_settings.save')]]</paper-button>
    </app-toolbar>

    <div class="form">
      <paper-input value="{{_name}}" label="[[localize('ui.dialogs.more_info_settings.name')]]"></paper-input>
    </div>
`}static get properties(){return{hass:Object,stateObj:Object,_componentLoaded:{type:Boolean,computed:"_computeComponentLoaded(hass)"},registryInfo:{type:Object,observer:"_registryInfoChanged",notify:!0},_name:String}}_computeStateName(e){return e?Object(n.a)(e):""}_computeComponentLoaded(e){return Object(O.a)(e,"config.entity_registry")}_registryInfoChanged(e){this._name=e?e.name:""}_backTapped(){this.fire("more-info-page",{page:null})}_save(){this.hass.connection.sendMessagePromise({type:"config/entity_registry/update",entity_id:this.stateObj.entity_id,name:this._name}).then(e=>{this.registryInfo=e.result},()=>{alert("save failed!")})}});var C=a(267);customElements.define("ha-more-info-dialog",class extends(Object(C.a)(s.a)){static get template(){return i["a"]`
    <style include="ha-style-dialog paper-dialog-shared-styles">
      :host {
        font-size: 14px;
        width: 365px;
        border-radius: 2px;
      }

      more-info-controls, more-info-settings {
        --more-info-header-background: var(--secondary-background-color);
        --more-info-header-color: var(--primary-text-color);
        --ha-more-info-app-toolbar-title: {
          /* Design guideline states 24px, changed to 16 to align with state info */
          margin-left: 16px;
          line-height: 1.3em;
          max-height: 2.6em;
          overflow: hidden;
          /* webkit and blink still support simple multiline text-overflow */
          display: -webkit-box;
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          text-overflow: ellipsis;
        }
      }

      /* overrule the ha-style-dialog max-height on small screens */
      @media all and (max-width: 450px), all and (max-height: 500px) {
        more-info-controls, more-info-settings {
          --more-info-header-background: var(--primary-color);
          --more-info-header-color: var(--text-primary-color);
        }
        :host {
          @apply --ha-dialog-fullscreen;
        }
        :host::before {
          content: "";
          position: fixed;
          z-index: -1;
          top: 0px;
          left: 0px;
          right: 0px;
          bottom: 0px;
          background-color: inherit;
        }
      }

      :host([data-domain=camera]) {
        width: auto;
      }

      :host([data-domain=history_graph]), :host([large]) {
        width: 90%;
      }
    </style>

    <template is="dom-if" if="[[!_page]]">
      <more-info-controls class="no-padding" hass="[[hass]]" state-obj="[[stateObj]]" dialog-element="[[_dialogElement]]" can-configure="[[_registryInfo]]" large="{{large}}"></more-info-controls>
    </template>
    <template is="dom-if" if="[[_equals(_page, &quot;settings&quot;)]]">
      <more-info-settings class="no-padding" hass="[[hass]]" state-obj="[[stateObj]]" registry-info="{{_registryInfo}}"></more-info-settings>
    </template>
`}static get properties(){return{hass:Object,stateObj:{type:Object,computed:"_computeStateObj(hass)",observer:"_stateObjChanged"},large:{type:Boolean,reflectToAttribute:!0,observer:"_largeChanged"},_dialogElement:Object,_registryInfo:Object,_page:{type:String,value:null},dataDomain:{computed:"_computeDomain(stateObj)",reflectToAttribute:!0}}}static get observers(){return["_dialogOpenChanged(opened)"]}ready(){super.ready(),this._dialogElement=this,this.addEventListener("more-info-page",e=>{this._page=e.detail.page})}_computeDomain(e){return e?Object(g.a)(e):""}_computeStateObj(e){return e.states[e.moreInfoEntityId]||null}_stateObjChanged(e,t){e?(!Object(O.a)(this.hass,"config.entity_registry")||t&&t.entity_id===e.entity_id||this.hass.connection.sendMessagePromise({type:"config/entity_registry/get",entity_id:e.entity_id}).then(e=>{this._registryInfo=e.result},()=>{this._registryInfo=!1}),requestAnimationFrame(()=>requestAnimationFrame(()=>{this.opened=!0}))):this.setProperties({opened:!1,_page:null,_registryInfo:null,large:!1})}_dialogOpenChanged(e){!e&&this.stateObj&&this.fire("hass-more-info",{entityId:null})}_equals(e,t){return e===t}_largeChanged(){this.notifyResize()}})}}]);
//# sourceMappingURL=8d4871a53279aa359cdb.chunk.js.map