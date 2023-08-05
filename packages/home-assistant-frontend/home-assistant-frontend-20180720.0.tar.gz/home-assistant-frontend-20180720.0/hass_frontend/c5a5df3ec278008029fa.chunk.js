(window.webpackJsonp=window.webpackJsonp||[]).push([[20],{203:function(t,e,i){"use strict";var s=i(0),a=i(3),n=(i(211),i(14));customElements.define("ha-call-service-button",class extends(Object(n.a)(a.a)){static get template(){return s["a"]`
    <ha-progress-button id="progress" progress="[[progress]]" on-click="buttonTapped"><slot></slot></ha-progress-button>
`}static get properties(){return{hass:{type:Object},progress:{type:Boolean,value:!1},domain:{type:String},service:{type:String},serviceData:{type:Object,value:{}}}}buttonTapped(){this.progress=!0;var t=this,e={domain:this.domain,service:this.service,serviceData:this.serviceData};this.hass.callService(this.domain,this.service,this.serviceData).then(function(){t.progress=!1,t.$.progress.actionSuccess(),e.success=!0},function(){t.progress=!1,t.$.progress.actionError(),e.success=!1}).then(function(){t.fire("hass-service-called",e)})}})},211:function(t,e,i){"use strict";i(60),i(127);var s=i(0),a=i(3);customElements.define("ha-progress-button",class extends a.a{static get template(){return s["a"]`
    <style>
      .container {
        position: relative;
        display: inline-block;
      }

      paper-button {
        transition: all 1s;
      }

      .success paper-button {
        color: white;
        background-color: var(--google-green-500);
        transition: none;
      }

      .error paper-button {
        color: white;
        background-color: var(--google-red-500);
        transition: none;
      }

      paper-button[disabled] {
        color: #c8c8c8;
      }

      .progress {
        @apply --layout;
        @apply --layout-center-center;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
      }
    </style>
    <div class="container" id="container">
      <paper-button id="button" disabled="[[computeDisabled(disabled, progress)]]" on-click="buttonTapped">
        <slot></slot>
      </paper-button>
      <template is="dom-if" if="[[progress]]">
        <div class="progress">
          <paper-spinner active=""></paper-spinner>
        </div>
      </template>
    </div>
`}static get properties(){return{hass:{type:Object},progress:{type:Boolean,value:!1},disabled:{type:Boolean,value:!1}}}tempClass(t){var e=this.$.container.classList;e.add(t),setTimeout(()=>{e.remove(t)},1e3)}ready(){super.ready(),this.addEventListener("click",t=>this.buttonTapped(t))}buttonTapped(t){this.progress&&t.stopPropagation()}actionSuccess(){this.tempClass("success")}actionError(){this.tempClass("error")}computeDisabled(t,e){return t||e}})},301:function(t,e,i){"use strict";i.d(e,"a",function(){return n});var s=i(260),a=i.n(s);function n(t){const e=a.a.map(t),i=document.createElement("link");return i.setAttribute("href","/static/images/leaflet/leaflet.css"),i.setAttribute("rel","stylesheet"),t.parentNode.appendChild(i),e.setView([51.505,-.09],13),a.a.tileLayer(`https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}${a.a.Browser.retina?"@2x.png":".png"}`,{attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',subdomains:"abcd",minZoom:0,maxZoom:20}).addTo(e),e}},302:function(t,e,i){"use strict";i(165);var s=i(0),a=i(3),n=i(14);customElements.define("ha-entity-marker",class extends(Object(n.a)(a.a)){static get template(){return s["a"]`
    <style include="iron-positioning"></style>
    <style>
    .marker {
      vertical-align: top;
      position: relative;
      display: block;
      margin: 0 auto;
      width: 2.5em;
      text-align: center;
      height: 2.5em;
      line-height: 2.5em;
      font-size: 1.5em;
      border-radius: 50%;
      border: 0.1em solid var(--ha-marker-color, var(--default-primary-color));
      color: rgb(76, 76, 76);
      background-color: white;
    }
    iron-image {
      border-radius: 50%;
    }
    </style>

    <div class="marker">
      <template is="dom-if" if="[[entityName]]">[[entityName]]</template>
      <template is="dom-if" if="[[entityPicture]]">
        <iron-image sizing="cover" class="fit" src="[[entityPicture]]"></iron-image>
      </template>
    </div>
`}static get properties(){return{hass:{type:Object},entityId:{type:String,value:""},entityName:{type:String,value:null},entityPicture:{type:String,value:null}}}ready(){super.ready(),this.addEventListener("click",t=>this.badgeTap(t))}badgeTap(t){t.stopPropagation(),this.entityId&&this.fire("hass-more-info",{entityId:this.entityId})}})},600:function(t,e,i){"use strict";i.r(e);var s=i(0),a=i(3);i(60),i(169),i(163),i(150),i(148),i(115),i(103),i(59),i(101),i(114),i(118),i(137),i(167);var n=i(14),r=i(75),o=(i(152),i(164),i(88),i(76));const c=["group","zone"];var l=i(96),h=(i(30),i(102),i(155),i(108)),d=i(36),p=i(67);const u=["cover","lock"];customElements.define("hui-entities-toggle",class extends a.a{static get template(){return s["a"]`
    <style>
      :host {
        width: 38px;
        display: block;
      }
      paper-toggle-button {
        cursor: pointer;
        --paper-toggle-button-label-spacing: 0;
        padding: 13px 5px;
        margin: -4px -5px;
      }
    </style>
    <template is="dom-if" if="[[_toggleEntities.length]]">
      <paper-toggle-button checked="[[_computeIsChecked(hass, _toggleEntities)]]" on-change="_callService"></paper-toggle-button>
    </template>
`}static get properties(){return{hass:Object,entities:Array,_toggleEntities:{type:Array,computed:"_computeToggleEntities(hass, entities)"}}}_computeToggleEntities(t,e){return e.filter(e=>e in t.states&&!u.includes(e.split(".",1)[0])&&Object(h.a)(t,t.states[e]))}_computeIsChecked(t,e){return e.some(e=>!d.g.includes(t.states[e].state))}_callService(t){const e=t.target.checked;!function(t,e,i=!0){const s={};e.forEach(e=>{if(d.g.includes(t.states[e].state)===i){const t=Object(p.a)(e),i=["cover","lock"].includes(t)?t:"homeassistant";i in s||(s[i]=[]),s[i].push(e)}}),Object.keys(s).forEach(e=>{let a;switch(e){case"lock":a=i?"unlock":"lock";break;case"cover":a=i?"open_cover":"close_cover";break;default:a=i?"turn_on":"turn_off"}const n=s[e];t.callService(e,a,{entity_id:n})})}(this.hass,this._toggleEntities,e)}}),i(117),i(156);var g=i(28);customElements.define("hui-generic-entity-row",class extends(Object(n.a)(a.a)){static get template(){return s["a"]`
      <style>
        :host {
          display: flex;
        }
        .flex {
          margin-left: 16px;
          flex: 1;
          display: flex;
          align-items: center;
          justify-content: space-between;
        }
        .secondary,
        ha-relative-time {
          display: block;
          color: var(--secondary-text-color);
        }
        .not-found {
          flex: 1;
          background-color: yellow;
          padding: 8px;
        }
      </style>
      <template is="dom-if" if="[[_stateObj]]">
        <state-badge state-obj="[[_stateObj]]"></state-badge>
        <div class="flex">
          <div class="info">
            [[_computeName(config.name, _stateObj)]]
            <template is="dom-if" if="[[config.secondary_info]]">
              <template is="dom-if" if="[[_equals(config.secondary_info, 'entity-id')]]">
                <div class="secondary">
                  [[_stateObj.entity_id]]
                </div>
              </template>
              <template is="dom-if" if="[[_equals(config.secondary_info, 'last-changed')]]">
                <ha-relative-time
                  hass="[[hass]]"
                  datetime="[[_stateObj.last_changed]]"
                ></ha-relative-time>
              </template>
            </template>
          </div>
          <slot></slot>
        </div>
      </template>
      <template is="dom-if" if="[[!_stateObj]]">
        <div class="not-found">
          Entity not available: [[config.entity]]
        </div>
      </template>
    `}static get properties(){return{hass:Object,config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, config.entity)"}}}_equals(t,e){return t===e}_computeStateObj(t,e){return t&&e in t?t[e]:null}_computeName(t,e){return t||Object(g.a)(e)}}),i(173),i(166);var m=i(79);customElements.define("hui-cover-entity-row",class extends a.a{static get template(){return s["a"]`
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
      >
        <template is="dom-if" if="[[!_entityObj.isTiltOnly]]">
          <ha-cover-controls hass="[[hass]]" state-obj="[[_stateObj]]"></ha-cover-controls>
        </template>
        <template is="dom-if" if="[[_entityObj.isTiltOnly]]">
          <ha-cover-tilt-controls hass="[[hass]]" state-obj="[[_stateObj]]"></ha-cover-tilt-controls>
        </template>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, _config.entity)"},_entityObj:{type:Object,computed:"_computeEntityObj(hass, _stateObj)"}}}_computeStateObj(t,e){return t&&e in t?t[e]:null}_computeEntityObj(t,e){return e?new m.a(t,e):null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}}),i(58),i(120);var f=i(43),_=i(45);customElements.define("hui-input-number-entity-row",class extends(Object(_.b)([f.a],a.a)){static get template(){return s["a"]`
      <style>
        .flex {
          display: flex;
          align-items: center;
        }
        .state {
          min-width: 45px;
          text-align: center;
        }
        paper-input {
          text-align: right;
        }
      </style>
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
        id="input_number_card"
      >
        <div>
          <template is="dom-if" if="[[_equals(_stateObj.attributes.mode, 'slider')]]">
            <div class="flex">
              <paper-slider
                min="[[_min]]"
                max="[[_max]]"
                value="{{_value}}"
                step="[[_step]]"
                pin
                on-change="_selectedValueChanged"
                ignore-bar-touch
              ></paper-slider>
              <div class="state">[[_value]] [[_stateObj.attributes.unit_of_measurement]]</div>
            </div>
          </template>
          <template is="dom-if" if="[[_equals(_stateObj.attributes.mode, 'box')]]">
            <paper-input
              no-label-float
              auto-validate
              pattern="[0-9]+([\\.][0-9]+)?"
              step="[[_step]]"
              min="[[_min]]"
              max="[[_max]]"
              value="{{_value}}"
              type="number"
              on-change="_selectedValueChanged"
            ></paper-input>
          </template>
        </div>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, _config.entity)",observer:"_stateObjChanged"},_min:{type:Number,value:0},_max:{type:Number,value:100},_step:Number,_value:Number}}ready(){super.ready(),"function"==typeof ResizeObserver?new ResizeObserver(t=>{t.forEach(()=>{this._hiddenState()})}).observe(this.$.input_number_card):this.addEventListener("iron-resize",this._hiddenState)}_equals(t,e){return t===e}_computeStateObj(t,e){return t&&e in t?t[e]:null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}_hiddenState(){if("slider"!==this._stateObj.attributes.mode)return;const t=this.shadowRoot.querySelector("paper-slider").offsetWidth,e=this.shadowRoot.querySelector(".state");t<100?e.style.display="none":t>=145&&(e.style.display="inline")}_stateObjChanged(t,e){this.setProperties({_min:Number(t.attributes.min),_max:Number(t.attributes.max),_step:Number(t.attributes.step),_value:Number(t.state)}),e&&"slider"===t.attributes.mode&&"slider"!==e.attributes.mode&&this._hiddenState()}_selectedValueChanged(){this._value!==Number(this._stateObj.state)&&this.hass.callService("input_number","set_value",{value:this._value,entity_id:this._stateObj.entity_id})}}),i(116),customElements.define("hui-input-select-entity-row",class extends(Object(n.a)(a.a)){static get template(){return s["a"]`
      <style>
        :host {
          display: flex;
          align-items: center;
        }
        paper-dropdown-menu {
          margin-left: 16px;
          flex: 1;
        }
        .not-found {
          flex: 1;
          background-color: yellow;
          padding: 8px;
        }
      </style>
      <template is="dom-if" if="[[_stateObj]]">
        <state-badge state-obj="[[_stateObj]]"></state-badge>
        <paper-dropdown-menu on-click="_stopPropagation" selected-item-label="{{_selected}}" label="[[_computeName(_config.name, _stateObj)]]">
          <paper-listbox slot="dropdown-content" selected="[[_computeSelected(_stateObj)]]">
            <template is="dom-repeat" items="[[_stateObj.attributes.options]]">
              <paper-item>[[item]]</paper-item>
            </template>
          </paper-listbox>
        </paper-dropdown-menu>
      </template>
      <template is="dom-if" if="[[!_stateObj]]">
        <div class="not-found">
          Entity not available: [[_config.entity]]
        </div>
      </template>
    `}static get properties(){return{hass:Object,_config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, _config.entity)"},_selected:{type:String,observer:"_selectedChanged"}}}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}_computeStateObj(t,e){return t&&e in t?t[e]:null}_computeName(t,e){return t||Object(g.a)(e)}_computeSelected(t){return t.attributes.options.indexOf(t.state)}_selectedChanged(t){""!==t&&t!==this._stateObj.state&&this.hass.callService("input_select","select_option",{option:t,entity_id:this._stateObj.entity_id})}_stopPropagation(t){t.stopPropagation()}}),customElements.define("hui-input-text-entity-row",class extends a.a{static get template(){return s["a"]`
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
      >
        <paper-input
          no-label-float
          minlength="[[_stateObj.attributes.min]]"
          maxlength="[[_stateObj.attributes.max]]"
          value="{{_value}}"
          auto-validate="[[_stateObj.attributes.pattern]]"
          pattern="[[_stateObj.attributes.pattern]]"
          type="[[_stateObj.attributes.mode]]"
          on-change="_selectedValueChanged"
          placeholder="(empty value)"
        ></paper-input>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, _config.entity)",observer:"_stateObjChanged"},_value:String}}_computeStateObj(t,e){return t&&e in t?t[e]:null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}_stateObjChanged(t){this._value=t.state}_selectedValueChanged(){this._value!==this._stateObj.state&&this.hass.callService("input_text","set_value",{value:this._value,entity_id:this._stateObj.entity_id})}});var b=i(18);customElements.define("hui-lock-entity-row",class extends(Object(b.a)(a.a)){static get template(){return s["a"]`
      <style>
        paper-button {
          color: var(--primary-color);
          font-weight: 500;
          margin: 0;
        }
      </style>
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
      >
        <paper-button on-click="_callService">
          [[_computeButtonTitle(_stateObj.state)]]
        </paper-button>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, _config.entity)"}}}_computeStateObj(t,e){return t&&e in t?t[e]:null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}_computeButtonTitle(t){return"locked"===t?this.localize("ui.card.lock.unlock"):this.localize("ui.card.lock.lock")}_callService(t){t.stopPropagation();const e=this._stateObj;this.hass.callService("lock","locked"===e.state?"unlock":"lock",{entity_id:e.entity_id})}}),customElements.define("hui-scene-entity-row",class extends(Object(b.a)(a.a)){static get template(){return s["a"]`
      <style>
        paper-button {
          color: var(--primary-color);
          font-weight: 500;
          margin: 0;
        }
      </style>
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
      >
        <paper-button on-click="_callService">
          [[localize('ui.card.scene.activate')]]
        </paper-button>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object}}_computeStateObj(t,e){return t&&e in t?t[e]:null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}_callService(t){t.stopPropagation(),this.hass.callService("scene","turn_on",{entity_id:this._config.entity})}}),i(121),customElements.define("hui-script-entity-row",class extends(Object(b.a)(a.a)){static get template(){return s["a"]`
      <style>
        paper-button {
          color: var(--primary-color);
          font-weight: 500;
          margin: 0;
        }
      </style>
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
      >
        <template is="dom-if" if="[[_stateObj.attributes.can_cancel]]">
          <ha-entity-toggle state-obj="[[_stateObj]]" hass="[[hass]]"></ha-entity-toggle>
        </template>
        <template is="dom-if" if="[[!_stateObj.attributes.can_cancel]]">
          <paper-button on-click="_callService">[[localize('ui.card.script.execute')]]</paper-button>
        </template>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, _config.entity)"}}}_computeStateObj(t,e){return t&&e in t?t[e]:null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}_callService(t){t.stopPropagation(),this.hass.callService("script","turn_on",{entity_id:this._config.entity})}});var y=i(104);customElements.define("hui-text-entity-row",class extends(Object(b.a)(a.a)){static get template(){return s["a"]`
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
      >
        <div>
          [[_computeState(_stateObj)]]
        </div>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, _config.entity)"}}}_computeStateObj(t,e){return t&&e in t?t[e]:null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}_computeState(t){return Object(y.a)(this.localize,t)}});var v=i(109),w=i(112);function C(t,e){return{type:"error",error:t,origConfig:e}}customElements.define("hui-timer-entity-row",class extends a.a{static get template(){return s["a"]`
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
      >
        <div>
          [[_computeDisplay(_stateObj, _timeRemaining)]]
        </div>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object,_stateObj:{type:Object,computed:"_computeStateObj(hass.states, _config.entity)",observer:"_stateObjChanged"},_timeRemaining:Number}}disconnectedCallback(){super.disconnectedCallback(),this._clearInterval()}_stateObjChanged(t){t?this._startInterval(t):this._clearInterval()}_clearInterval(){this._updateRemaining&&(clearInterval(this._updateRemaining),this._updateRemaining=null)}_startInterval(t){this._clearInterval(),this._calculateRemaining(t),"active"===t.state&&(this._updateRemaining=setInterval(()=>this._calculateRemaining(this._stateObj),1e3))}_calculateRemaining(t){this._timeRemaining=Object(v.a)(t)}_computeDisplay(t,e){if("idle"===t.state||0===e)return t.state;let i=Object(w.a)(e);return"paused"===t.state&&(i+=" (paused)"),i}_computeStateObj(t,e){return t&&e in t?t[e]:null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}}),customElements.define("hui-toggle-entity-row",class extends a.a{static get template(){return s["a"]`
      <hui-generic-entity-row
        hass="[[hass]]"
        config="[[_config]]"
      >
        <ha-entity-toggle hass="[[hass]]" state-obj="[[_computeStateObj(hass.states, _config.entity)]]"></ha-entity-toggle>
      </hui-generic-entity-row>
    `}static get properties(){return{hass:Object,_config:Object}}_computeStateObj(t,e){return t&&e in t?t[e]:null}setConfig(t){if(!t||!t.entity)throw new Error("Entity not configured.");this._config=t}});const j="custom:",O={cover:"cover",fan:"toggle",group:"toggle",input_boolean:"toggle",input_number:"input-number",input_select:"input-select",input_text:"input-text",light:"toggle",lock:"lock",scene:"scene",script:"script",timer:"timer",switch:"toggle"};function x(t,e){const i=document.createElement(t);try{"setConfig"in i&&i.setConfig(e)}catch(i){return console.error(t,i),E(i.message,e)}return i}function E(t,e){return x("hui-error-card",C(t,e))}function k(t){let e;if(!t||"object"!=typeof t||!t.entity)return E("Invalid config given.",t);const i=t.type||"default";if(i.startsWith(j)){if(e=i.substr(j.length),customElements.get(e))return x(e,t);const s=E(`Custom element doesn't exist: ${e}.`,t);return customElements.whenDefined(e).then(()=>Object(l.a)(s,"rebuild-view")),s}const s=t.entity.split(".",1)[0];return x(e=`hui-${O[s]||"text"}-entity-row`,t)}function S(t){if(!t||!Array.isArray(t))throw new Error("Entities need to be an array");return t.map((t,i)=>{if("string"==typeof t)t={entity:t};else{if("object"!=typeof t||Array.isArray(t))throw new Error(`Invalid entity specified at position ${i}.`);if(!t.entity)throw new Error(`Entity object at position ${i} is missing entity field.`)}if(e=t.entity,!/^(\w+)\.(\w+)$/.test(e))throw new Error(`Invalid entity ID at position ${i}: ${t.entity}`);return t});var e}function I(t,e,i=!0){const s=Object(p.a)(e),a="group"===s?"homeassistant":s;let n;switch(s){case"lock":n=i?"unlock":"lock";break;case"cover":n=i?"open_cover":"close_cover";break;default:n=i?"turn_on":"turn_off"}t.callService(a,n,{entity_id:e})}function $(t,e){I(t,e,d.g.includes(t.states[e].state))}function z(t){return"function"==typeof t.getCardSize?t.getCardSize():1}customElements.define("hui-entities-card",class extends(Object(n.a)(a.a)){static get template(){return s["a"]`
    <style>
      ha-card {
        padding: 16px;
      }
      #states {
        margin: -4px 0;
      }
      #states > div {
        margin: 4px 0;
      }
      .header {
        @apply --paper-font-headline;
        /* overwriting line-height +8 because entity-toggle can be 40px height,
           compensating this with reduced padding */
        line-height: 40px;
        color: var(--primary-text-color);
        padding: 4px 0 12px;
        display: flex;
        justify-content: space-between;
      }
      .header .name {
        @apply --paper-font-common-nowrap;
      }
      .state-card-dialog {
        cursor: pointer;
      }
    </style>

    <ha-card>
      <template is='dom-if' if='[[_showHeader(_config)]]'>
        <div class='header'>
          <div class="name">[[_config.title]]</div>
          <template is="dom-if" if="[[_showHeaderToggle(_config.show_header_toggle)]]">
            <hui-entities-toggle hass="[[hass]]" entities="[[_config.entities]]"></hui-entities-toggle>
          </template>
        </div>
      </template>
      <div id="states"></div>
    </ha-card>
`}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},_config:Object}}constructor(){super(),this._elements=[]}ready(){super.ready(),this._config&&this._buildConfig()}getCardSize(){return 1+(this._config?this._config.entities.length:0)}_showHeaderToggle(t){return!1!==t}_showHeader(t){return t.title||t.show_header_toggle}setConfig(t){this._config=t,this._configEntities=S(t.entities),this.$&&this._buildConfig()}_buildConfig(){const t=this.$.states,e=this._configEntities;for(;t.lastChild;)t.removeChild(t.lastChild);this._elements=[];for(const i of e){const e=i.entity,s=k(i);e&&!d.c.includes(Object(p.a)(e))&&(s.classList.add("state-card-dialog"),s.addEventListener("click",()=>this.fire("hass-more-info",{entityId:e}))),s.hass=this.hass,this._elements.push(s);const a=document.createElement("div");a.appendChild(s),t.appendChild(a)}}_hassChanged(t){this._elements.forEach(e=>{e.hass=t})}}),customElements.define("hui-entity-filter-card",class extends a.a{static get properties(){return{hass:{type:Object,observer:"_hassChanged"}}}getCardSize(){return this.lastChild?this.lastChild.getCardSize():1}setConfig(t){if(!t.state_filter||!Array.isArray(t.state_filter))throw new Error("Incorrect filter config.");this._config=t,this._configEntities=S(t.entities),this.lastChild&&(this.removeChild(this.lastChild),this._element=null);const e="card"in t?Object.assign({},t.card):{};e.type||(e.type="entities"),e.entities=[];const i=G(e);i._filterRawConfig=e,this._updateCardConfig(i),this._element=i}_hassChanged(){this._updateCardConfig(this._element)}_updateCardConfig(t){if(!t||"HUI-ERROR-CARD"===t.tagName||!this.hass)return;const e=(i=this.hass,s=this._config.state_filter,this._configEntities.filter(t=>{const e=i.states[t.entity];return e&&s.includes(e.state)}));var i,s;0!==e.length||!1!==this._config.show_empty?(this.style.display="block",t.setConfig(Object.assign({},t._filterRawConfig,{entities:e})),t.isPanel=this.isPanel,t.hass=this.hass,this.lastChild||this.appendChild(t)):this.style.display="none"}}),customElements.define("hui-error-card",class extends a.a{static get template(){return s["a"]`
      <style>
        :host {
          display: block;
          background-color: red;
          color: white;
          padding: 8px;
        }
      </style>
      [[_config.error]]
      <pre>[[_toStr(_config.origConfig)]]</pre>
    `}static get properties(){return{_config:Object}}setConfig(t){this._config=t}getCardSize(){return 4}_toStr(t){return JSON.stringify(t,null,2)}}),customElements.define("hui-glance-card",class extends(Object(b.a)(Object(n.a)(a.a))){static get template(){return s["a"]`
      <style>
        ha-card {
          padding: 16px;
        }
        ha-card[header] {
          padding-top: 0;
        }
        .entities {
          display: flex;
          margin-bottom: -12px;
          flex-wrap: wrap;
        }
        .entity {
          box-sizing: border-box;
          padding: 0 4px;
          display: flex;
          flex-direction: column;
          align-items: center;
          cursor: pointer;
          margin-bottom: 12px;
          width: var(--glance-column-width, 20%);
        }
        .entity div {
          width: 100%;
          text-align: center;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }
      </style>

      <ha-card header$="[[_config.title]]">
        <div class="entities">
          <template is="dom-repeat" items="[[_configEntities]]">
            <template is="dom-if" if="[[_showEntity(item, hass.states)]]">
              <div class="entity" on-click="_handleClick">
                <template is="dom-if" if="[[_showInfo(_config.show_name)]]">
                  <div>[[_computeName(item, hass.states)]]</div>
                </template>
                <state-badge state-obj="[[_computeStateObj(item, hass.states)]]"></state-badge>
                <template is="dom-if" if="[[_showInfo(_config.show_state)]]">
                  <div>[[_computeState(item, hass.states)]]</div>
                </template>
              </div>
            </template>
          </template>
        </div>
      </ha-card>
    `}static get properties(){return{hass:Object,_config:Object,_configEntities:Array}}getCardSize(){return 3}setConfig(t){this._config=t,this.updateStyles({"--glance-column-width":t&&t.column_width||"20%"}),this._configEntities=S(t.entities)}_showEntity(t,e){return t.entity in e}_showInfo(t){return!1!==t}_computeName(t,e){return t.name||Object(g.a)(e[t.entity])}_computeStateObj(t,e){return e[t.entity]}_computeState(t,e){return Object(y.a)(this.localize,e[t.entity])}_handleClick(t){const e=t.model.item.entity;switch(t.model.item.tap_action){case"toggle":$(this.hass,e);break;case"turn-on":I(this.hass,e,!0);break;default:this.fire("hass-more-info",{entityId:e})}}}),i(157),i(159),customElements.define("hui-history-graph-card",class extends a.a{static get template(){return s["a"]`
      <style>
        ha-card {
          padding: 16px;
        }
        ha-card[header] {
          padding-top: 0;
        }
      </style>

      <ha-card header$='[[_config.title]]'>
        <ha-state-history-data
          hass="[[hass]]"
          filter-type="recent-entity"
          entity-id="[[_entities]]"
          data="{{stateHistory}}"
          is-loading="{{stateHistoryLoading}}"
          cache-config="[[_computeCacheConfig(_config)]]"
        ></ha-state-history-data>
        <state-history-charts
          hass="[[hass]]"
          history-data="[[stateHistory]]"
          is-loading-data="[[stateHistoryLoading]]"
          names="[[_names]]"
          up-to-now
          no-single
        ></state-history-charts>
      </ha-card>
    `}static get properties(){return{hass:Object,_config:Object,stateHistory:{type:Object},_names:Array,_entities:Object,stateHistoryLoading:Boolean}}getCardSize(){return 4}setConfig(t){const e=S(t.entities);this._config=t;const i=[],s={};for(const t of e)i.push(t.entity),t.name&&(s[t.entity]=t.name);this._entities=i,this._names=s}_computeCacheConfig(t){return{cacheKey:t.entities,hoursToShow:t.hours_to_show||24,refresh:t.refresh_interval||0}}}),customElements.define("hui-horizontal-stack-card",class extends a.a{static get template(){return s["a"]`
      <style>
        #root {
          display: flex;
        }
        #root > * {
          flex: 1 1 0;
          margin: 0 4px;
        }
        #root > *:first-child {
          margin-left: 0;
        }
        #root > *:last-child {
          margin-right: 0;
        }
      </style>
      <div id="root"></div>
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"}}}constructor(){super(),this._elements=[]}ready(){super.ready(),this._config&&this._buildConfig()}getCardSize(){let t=1;return this._elements.forEach(e=>{const i=z(e);i>t&&(t=i)}),t}setConfig(t){if(!t||!t.cards||!Array.isArray(t.cards))throw new Error("Card config incorrect.");this._config=t,this.$&&this._buildConfig()}_buildConfig(){const t=this._config;this._elements=[];const e=this.$.root;for(;e.lastChild;)e.removeChild(e.lastChild);const i=[];t.cards.forEach(t=>{const s=G(t);s.hass=this.hass,i.push(s),e.appendChild(s)}),this._elements=i}_hassChanged(t){this._elements.forEach(e=>{e.hass=t})}}),customElements.define("hui-iframe-card",class extends a.a{static get template(){return s["a"]`
      <style>
        ha-card {
          overflow: hidden;
        }
        #root {
          width: 100%;
          position: relative;
        }
        iframe {
          border: none;
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
        }
      </style>
      <ha-card header="[[_config.title]]">
        <div id="root">
          <iframe src="[[_config.url]]"></iframe>
        </div>
      </ha-card>
    `}static get properties(){return{_config:Object}}ready(){super.ready(),this._config&&this._buildConfig()}setConfig(t){this._config=t,this.$&&this._buildConfig()}_buildConfig(){const t=this._config;this.$.root.style.paddingTop=t.aspect_ratio||"50%"}getCardSize(){return 1+this.offsetHeight/50}});var T=i(260),L=i.n(T),A=(i(302),i(301)),R=i(26);function N(t,e,i){let s;return function(...a){const n=this,r=i&&!s;clearTimeout(s),s=setTimeout(()=>{s=null,i||t.apply(n,a)},e),r&&t.apply(n,a)}}L.a.Icon.Default.imagePath="/static/images/leaflet",customElements.define("hui-map-card",class extends a.a{static get template(){return s["a"]`
      <style>
        :host([is-panel]) ha-card {
          left: 0;
          top: 0;
          width: 100%;
          /**
           * In panel mode we want a full height map. Since parent #view
           * only sets min-height, we need absolute positioning here
           */
          height: 100%;
          position: absolute;
        }

        ha-card {
          overflow: hidden;
        }

        #map {
          z-index: 0;
          border: none;
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
        }

        paper-icon-button {
          position: absolute;
          top: 75px;
          left: 7px;
        }

        #root {
          position: relative;
        }

        :host([is-panel]) #root {
          height: 100%;
        }
      </style>

      <ha-card id="card" header="[[_config.title]]">
        <div id="root">
          <div id="map"></div>
          <paper-icon-button
            on-click="_fitMap"
            icon="hass:image-filter-center-focus"
            title="Reset focus"
          ></paper-icon-button>
        </div>
      </ha-card>

    `}static get properties(){return{hass:{type:Object,observer:"_drawEntities"},_config:Object,isPanel:{type:Boolean,reflectToAttribute:!0}}}constructor(){super(),this._debouncedResizeListener=N(this._resetMap.bind(this),100)}ready(){super.ready(),this._config&&!this.isPanel&&(this.$.root.style.paddingTop=this._config.aspect_ratio||"100%")}setConfig(t){if(!t)throw new Error("Error in card configuration.");this._configEntities=S(t.entities),this._config=t}getCardSize(){let t=this._config.aspect_ratio||"100%";return t=t.substr(0,t.length-1),1+Math.floor(t/25)||3}connectedCallback(){super.connectedCallback(),"function"==typeof ResizeObserver?(this._resizeObserver=new ResizeObserver(()=>this._debouncedResizeListener()),this._resizeObserver.observe(this.$.map)):window.addEventListener("resize",this._debouncedResizeListener),this._map=Object(A.a)(this.$.map),this._drawEntities(this.hass),setTimeout(()=>{this._resetMap(),this._fitMap()},1)}disconnectedCallback(){super.disconnectedCallback(),this._map&&this._map.remove(),this._resizeObserver?this._resizeObserver.unobserve(this.$.map):window.removeEventListener("resize",this._debouncedResizeListener)}_resetMap(){this._map&&this._map.invalidateSize()}_fitMap(){if(0===this._mapItems.length)this._map.setView(new L.a.LatLng(this.hass.config.core.latitude,this.hass.config.core.longitude),14);else{const t=new L.a.latLngBounds(this._mapItems.map(t=>t.getLatLng()));this._map.fitBounds(t.pad(.5))}}_drawEntities(t){const e=this._map;if(!e)return;this._mapItems&&this._mapItems.forEach(t=>t.remove());const i=this._mapItems=[];this._configEntities.forEach(s=>{const a=s.entity;if(!(a in t.states))return;const n=t.states[a],r=Object(g.a)(n),{latitude:o,longitude:c,passive:l,icon:h,radius:d,entity_picture:p,gps_accuracy:u}=n.attributes;if(!o||!c)return;let m,f,_;if("zone"===Object(R.a)(n)){if(l)return;return h?((_=document.createElement("ha-icon")).setAttribute("icon",h),f=_.outerHTML):f=r,m=L.a.divIcon({html:f,iconSize:[24,24],className:""}),i.push(L.a.marker([o,c],{icon:m,interactive:!1,title:r}).addTo(e)),void i.push(L.a.circle([o,c],{interactive:!1,color:"#FF9800",radius:d}).addTo(e))}const b=r.split(" ").map(t=>t[0]).join("").substr(0,3);(_=document.createElement("ha-entity-marker")).setAttribute("entity-id",a),_.setAttribute("entity-name",b),_.setAttribute("entity-picture",p||""),m=L.a.divIcon({html:_.outerHTML,iconSize:[48,48],className:""}),i.push(L.a.marker([o,c],{icon:m,title:Object(g.a)(n)}).addTo(e)),u&&i.push(L.a.circle([o,c],{interactive:!1,color:"#0288D1",radius:u}).addTo(e))})}}),i(154),customElements.define("hui-markdown-card",class extends a.a{static get template(){return s["a"]`
      <style>
        :host {
          @apply --paper-font-body1;
        }
        ha-markdown {
          display: block;
          padding: 0 16px 16px;
          -ms-user-select: initial;
          -webkit-user-select: initial;
          -moz-user-select: initial;
        }
        :host([no-title]) ha-markdown {
          padding-top: 16px;
        }
        ha-markdown > *:first-child {
          margin-top: 0;
        }
        ha-markdown > *:last-child {
          margin-bottom: 0;
        }
        ha-markdown a {
          color: var(--primary-color);
        }
        ha-markdown img {
          max-width: 100%;
        }
      </style>
      <ha-card header="[[_config.title]]">
        <ha-markdown content='[[_config.content]]'></ha-markdown>
      </ha-card>
    `}static get properties(){return{_config:Object,noTitle:{type:Boolean,reflectToAttribute:!0,computed:"_computeNoTitle(_config.title)"}}}setConfig(t){this._config=t}getCardSize(){return this._config.content.split("\n").length}_computeNoTitle(t){return!t}}),i(171);class D extends HTMLElement{constructor(t,e){super(),this._tag=t.toUpperCase(),this._domain=e,this._element=null}getCardSize(){return 3}setConfig(t){if(!t.entity)throw new Error("No entity specified");if(Object(p.a)(t.entity)!==this._domain)throw new Error(`Specified entity needs to be of domain ${this._domain}.`);this._config=t}set hass(t){const e=this._config.entity;e in t.states?(this._ensureElement(this._tag),this.lastChild.hass=t,this.lastChild.stateObj=t.states[e]):(this._ensureElement("HUI-ERROR-CARD"),this.lastChild.setConfig(C(`No state available for ${e}`,this._config)))}_ensureElement(t){this.lastChild&&this.lastChild.tagName===t||(this.lastChild&&this.removeChild(this.lastChild),this.appendChild(document.createElement(t)))}}customElements.define("hui-media-control-card",class extends D{constructor(){super("ha-media_player-card","media_player")}}),customElements.define("hui-picture-card",class extends(Object(r.a)(a.a)){static get template(){return s["a"]`
      <style>
        ha-card {
          overflow: hidden;
        }
        ha-card[clickable] {
          cursor: pointer;
        }
        img {
          display: block;
          width: 100%;
        }
      </style>

      <ha-card on-click="_cardClicked" clickable$='[[_computeClickable(_config)]]'>
        <img src='[[_config.image]]' />
      </ha-card>
    `}static get properties(){return{hass:Object,_config:Object}}getCardSize(){return 3}setConfig(t){if(!t||!t.image)throw new Error("Error in card configuration.");this._config=t}_computeClickable(t){return t.navigation_path||t.service}_cardClicked(){if(this._config.navigation_path&&this.navigate(this._config.navigation_path),this._config.service){const[t,e]=this._config.service.split(".",2);this.hass.callService(t,e,this._config.service_data)}}});var H=i(6),P=Object(H.a)(t=>(class extends(Object(r.a)(Object(n.a)(t))){handleClick(t,e){const i=e.tap_action||"more-info";if("none"!==i)switch(i){case"more-info":this.fire("hass-more-info",{entityId:e.entity});break;case"navigate":this.navigate(e.navigation_path);break;case"toggle":$(t,e.entity);break;case"call-service":{const[i,s]=e.service.split(".",2),a=Object.assign({},{entity_id:e.entity},e.service_data);t.callService(i,s,a)}}}computeTooltip(t,e){if(e.title)return e.title;const i=e.entity in t.states?Object(g.a)(t.states[e.entity]):e.entity;let s;switch(e.tap_action){case"navigate":s=`Navigate to ${e.navigation_path}`;break;case"toggle":s=`Toggle ${i}`;break;case"call-service":s=`Call service ${e.service}`;break;default:s=`Show more-info: ${i}`}return s}}));customElements.define("hui-icon-element",class extends(P(a.a)){static get template(){return s["a"]`
      <style>
        :host {
          cursor: pointer; 
        } 
      </style>
      <ha-icon 
        icon="[[_config.icon]]"
        title$="[[computeTooltip(hass, _config)]]"
      ></ha-icon> 
    `}static get properties(){return{hass:Object,_config:Object}}ready(){super.ready(),this.addEventListener("click",()=>this.handleClick(this.hass,this._config))}setConfig(t){if(!t||!t.icon)throw Error("Error in element configuration");this._config=t}});customElements.define("hui-image",class extends(Object(b.a)(a.a)){static get template(){return s["a"]`
      <style>
        img {
          display: block;
          height: auto;
          transition: filter .2s linear;
          width: 100%;
        }

        .error {
          text-align: center;
        }

        .hidden {
          display: none;
        }

        #brokenImage {
          background: grey url('/static/images/image-broken.svg') center/36px no-repeat;
        }

      </style>

      <img
        id="image"
        src="[[_imageSrc]]"
        on-error="_onImageError"
        on-load="_onImageLoad" />
      <div id="brokenImage"></div>
`}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},entity:String,image:String,stateImage:Object,cameraImage:String,filter:String,stateFilter:Object,_imageSrc:String}}static get observers(){return["_configChanged(image, stateImage, cameraImage)"]}connectedCallback(){super.connectedCallback(),this.cameraImage&&(this.timer=setInterval(()=>this._updateCameraImageSrc(),1e4))}disconnectedCallback(){super.disconnectedCallback(),clearInterval(this.timer)}_configChanged(t,e,i){i?this._updateCameraImageSrc():t&&!e&&(this._imageSrc=t)}_onImageError(){this._imageSrc=null,this.$.image.classList.add("hidden"),this.$.brokenImage.style.setProperty("height",`${this._lastImageHeight||"100"}px`),this.$.brokenImage.classList.remove("hidden")}_onImageLoad(){this.$.image.classList.remove("hidden"),this.$.brokenImage.classList.add("hidden"),this._lastImageHeight=this.$.image.offsetHeight}_hassChanged(t){if(this.cameraImage||!this.entity)return;const e=t.states[this.entity],i=e?e.state:"unavailable";i!==this._currentState&&(this._currentState=i,this._updateStateImage(),this._updateStateFilter(e))}_updateStateImage(){if(!this.stateImage)return void(this._imageFallback=!0);const t=this.stateImage[this._currentState];this._imageSrc=t||this.image,this._imageFallback=!t}_updateStateFilter(t){let e;e=this.stateFilter&&this.stateFilter[this._currentState]||this.filter;const i=!t||d.g.includes(t.state);this.$.image.style.filter=e||i&&this._imageFallback&&"grayscale(100%)"||""}async _updateCameraImageSrc(){try{const{content_type:t,content:e}=await this.hass.callWS({type:"camera_thumbnail",entity_id:this.cameraImage});this._imageSrc=`data:${t};base64, ${e}`,this._onImageLoad()}catch(t){this._onImageError()}}}),customElements.define("hui-image-element",class extends(P(a.a)){static get template(){return s["a"]`
      <style>
        :host(.clickable) {
          cursor: pointer; 
        } 
        hui-image {
          overflow-y: hidden;
        } 
      </style>
      <hui-image
        hass="[[hass]]"
        entity="[[_config.entity]]"
        image="[[_config.image]]"
        state-image="[[_config.state_image]]"
        camera-image="[[_config.camera_image]]"
        filter="[[_config.filter]]"
        state-filter="[[_config.state_filter]]"
        title$="[[computeTooltip(hass, _config)]]"
      ></hui-image>
    `}static get properties(){return{hass:Object,_config:Object}}ready(){super.ready(),this.addEventListener("click",()=>this.handleClick(this.hass,this._config))}setConfig(t){if(!t)throw Error("Error in element configuration");this.classList.toggle("clickable","none"!==t.tap_action),this._config=t}}),i(203),customElements.define("hui-service-button-element",class extends a.a{static get template(){return s["a"]`
      <style>
        ha-call-service-button {
          color: var(--primary-color);
          white-space: nowrap;
        }
      </style>
      <ha-call-service-button 
        hass="[[hass]]"
        domain="[[_domain]]" 
        service="[[_service]]"
        serviceData="[[_config.serviceData]]"
      >[[_config.title]]</ha-call-service-button> 
    `}static get properties(){return{hass:Object,_config:Object,_domain:String,_service:String}}setConfig(t){if(!t||!t.service)throw Error("Error in element configuration");const[e,i]=t.service.split(".",2);this.setProperties({_config:t,_domain:e,_service:i})}}),i(160),customElements.define("hui-state-badge-element",class extends a.a{static get properties(){return{hass:Object,_config:Object}}static get observers(){return["_updateBadge(hass, _config)"]}_updateBadge(t,e){if(!(t&&e&&e.entity in t.states))return;this._badge||(this._badge=document.createElement("ha-state-label-badge"));const i=t.states[e.entity];this._badge.state=i,this._badge.setAttribute("title",Object(g.a)(i)),this.lastChild||this.appendChild(this._badge)}setConfig(t){if(!t||!t.entity)throw Error("Error in element configuration");this.lastChild&&this.removeChild(this.lastChild),this._badge=null,this._config=t}}),customElements.define("hui-state-icon-element",class extends(P(a.a)){static get template(){return s["a"]`
      <style>
        :host {
          cursor: pointer; 
        } 
      </style>
      <state-badge 
        state-obj="[[_stateObj]]"
        title$="[[computeTooltip(hass, _config)]]"
      ></state-badge> 
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},_config:Object,_stateObj:Object}}ready(){super.ready(),this.addEventListener("click",()=>this.handleClick(this.hass,this._config))}setConfig(t){if(!t||!t.entity)throw Error("Error in element configuration");this._config=t}_hassChanged(t){this._stateObj=t.states[this._config.entity]}}),customElements.define("hui-state-label-element",class extends(Object(b.a)(P(a.a))){static get template(){return s["a"]`
      <style>
        :host {
          cursor: pointer; 
        } 
        .state-label {
          padding: 8px;
          white-space: nowrap;
        }
      </style>
      <div class="state-label" title$="[[computeTooltip(hass, _config)]]"> 
        [[_computeStateDisplay(_stateObj)]]
      </div>
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},_config:Object,_stateObj:Object}}ready(){super.ready(),this.addEventListener("click",()=>this.handleClick(this.hass,this._config))}setConfig(t){if(!t||!t.entity)throw Error("Error in element configuration");this._config=t}_hassChanged(t){this._stateObj=t.states[this._config.entity]}_computeStateDisplay(t){return t&&Object(y.a)(this.localize,t)}});const V=new Set(["icon","image","service-button","state-badge","state-icon","state-label"]);function M(t,e){const i=document.createElement(t);try{i.setConfig(e)}catch(i){return console.error(t,i),B(i.message,e)}return i}function B(t,e){return M("hui-error-card",C(t,e))}customElements.define("hui-picture-elements-card",class extends a.a{static get template(){return s["a"]`
    <style>
      ha-card {
        overflow: hidden;
      }
      #root {
        position: relative;
        overflow: hidden;
      }
      #root img {
        display: block;
        width: 100%;
      }
      .element {
        position: absolute;
        transform: translate(-50%, -50%);
      }
      hui-image-element {
        overflow-y: hidden;
      }
    </style>

    <ha-card header="[[_config.title]]">
      <div id="root"></div>
    </ha-card>
`}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},_config:Object}}constructor(){super(),this._elements=[]}ready(){super.ready(),this._config&&this._buildConfig()}getCardSize(){return 4}setConfig(t){if(!t||!t.image||!Array.isArray(t.elements))throw new Error("Invalid card configuration");this._config=t,this.$&&this._buildConfig()}_buildConfig(){const t=this._config,e=this.$.root;for(this._elements=[];e.lastChild;)e.removeChild(e.lastChild);const i=document.createElement("img");i.src=t.image,e.appendChild(i),t.elements.forEach(t=>{const i=function(t){if(!t||"object"!=typeof t||!t.type)return B("No element type configured.",t);if(t.type.startsWith("custom:")){const e=t.type.substr("custom:".length);if(customElements.get(e))return M(e,t);const i=B(`Custom element doesn't exist: ${e}.`,t);return customElements.whenDefined(e).then(()=>Object(l.a)(i,"rebuild-view")),i}return V.has(t.type)?M(`hui-${t.type}-element`,t):B(`Unknown element type encountered: ${t.type}.`,t)}(t);i.hass=this.hass,this._elements.push(i),i.classList.add("element"),Object.keys(t.style).forEach(e=>{i.style.setProperty(e,t.style[e])}),e.appendChild(i)}),this.hass&&this._hassChanged(this.hass)}_hassChanged(t){this._elements.forEach(e=>{e.hass=t})}});customElements.define("hui-picture-entity-card",class extends(Object(n.a)(Object(b.a)(a.a))){static get template(){return s["a"]`
      <style>
        ha-card {
          min-height: 75px;
          overflow: hidden;
          position: relative;
        }
        ha-card.canInteract {
          cursor: pointer;
        }
        .info {
          @apply --paper-font-common-nowrap;
          position: absolute;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: rgba(0, 0, 0, 0.3);
          padding: 16px;
          font-size: 16px;
          line-height: 16px;
          color: white;
          display: flex;
          justify-content: space-between;
        }
        #title {
          font-weight: 500;
        }
        [hidden] {
          display: none;
        }
      </style>

      <ha-card id='card' on-click="_cardClicked">
        <hui-image
          hass="[[hass]]"
          image="[[_config.image]]"
          state-image="[[_config.state_image]]"
          camera-image="[[_getCameraImage(_config)]]" 
          entity="[[_config.entity]]"
        ></hui-image>
        <div class="info" hidden$='[[_computeHideInfo(_config)]]'>
          <div id="name"></div>
          <div id="state"></div>
        </div>
      </ha-card>
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},_config:Object}}getCardSize(){return 3}setConfig(t){if(!t||!t.entity)throw new Error("Error in card configuration.");if(this._entityDomain=Object(p.a)(t.entity),"camera"!==this._entityDomain&&!t.image&&!t.state_image&&!t.camera_image)throw new Error("No image source configured.");this._config=t}_hassChanged(t){const e=this._config,i=e.entity,s=t.states[i];if(!s&&"Unavailable"===this._oldState||s&&s.state===this._oldState)return;let a,n,r,o=!0;s?(a=e.name||Object(g.a)(s),n=s.state,r=this._computeStateLabel(s)):(a=e.name||i,n="Unavailable",r="Unavailable",o=!1),this.$.name.innerText=a,this.$.state.innerText=r,this._oldState=n,this.$.card.classList.toggle("canInteract",o)}_computeStateLabel(t){switch(this._entityDomain){case"scene":return this.localize("ui.card.scene.activate");case"script":return this.localize("ui.card.script.execute");case"weblink":return"Open";default:return Object(y.a)(this.localize,t)}}_computeHideInfo(t){return!1===t.show_info}_cardClicked(){const t=this._config&&this._config.entity;t&&t in this.hass.states&&("toggle"===this._config.tap_action?"weblink"===this._entityDomain?window.open(this.hass.states[t].state):$(this.hass,t):this.fire("hass-more-info",{entityId:t}))}_getCameraImage(t){return"camera"===this._entityDomain?t.entity:t.camera_image}});var q=i(110);const F=new Set(["input_boolean","light","switch"]),U=new Set(["closed","locked","not_home","off"]);customElements.define("hui-picture-glance-card",class extends(Object(r.a)(Object(b.a)(Object(n.a)(a.a)))){static get template(){return s["a"]`
      <style>
        ha-card {
          position: relative;
          min-height: 48px;
          overflow: hidden;
        }
        hui-image.clickable {
          cursor: pointer;
        }
        .box {
          @apply --paper-font-common-nowrap;
          position: absolute;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: rgba(0, 0, 0, 0.3);
          padding: 4px 8px;
          font-size: 16px;
          line-height: 40px;
          color: white;
          display: flex;
          justify-content: space-between;
        }
        .box .title {
          font-weight: 500;
          margin-left: 8px;
        }
        paper-icon-button {
          color: #A9A9A9;
        }
        paper-icon-button.state-on {
          color: white;
        }
      </style>

      <ha-card>
        <hui-image
          class$='[[_computeImageClass(_config)]]'
          on-click='_handleImageClick'
          hass="[[hass]]"
          image="[[_config.image]]"
          state-image="[[_config.state_image]]"
          camera-image="[[_config.camera_image]]"
          entity="[[_config.entity]]"
        ></hui-image>
        <div class="box">
          <template is="dom-if" if="[[_config.title]]">
            <div class="title">[[_config.title]]</div>
          </template>
          <div>
            <template is="dom-repeat" items="[[_computeVisible(_entitiesDialog, hass.states)]]">
              <paper-icon-button
                on-click="_openDialog"
                class$="[[_computeButtonClass(item.entity, hass.states)]]"
                icon="[[_computeIcon(item.entity, hass.states)]]"
                title="[[_computeTooltip(item.entity, hass.states)]]"
              ></paper-icon-button>
            </template>
          </div>
          <div>
            <template is="dom-repeat" items="[[_computeVisible(_entitiesToggle, hass.states)]]">
              <paper-icon-button
                on-click="_callService"
                class$="[[_computeButtonClass(item.entity, hass.states)]]"
                icon="[[_computeIcon(item.entity, hass.states)]]"
                title="[[_computeTooltip(item.entity, hass.states)]]"
              ></paper-icon-button>
            </template>
          </div>
        </div>
      </ha-card>
    `}static get properties(){return{hass:Object,_config:Object,_entitiesDialog:Array,_entitiesToggle:Array}}getCardSize(){return 3}setConfig(t){if(!t||!t.entities||!Array.isArray(t.entities)||!(t.image||t.camera_image||t.state_image)||t.state_image&&!t.entity)throw new Error("Invalid card configuration");const e=[],i=[];S(t.entities).forEach(s=>{t.force_dialog||!F.has(Object(p.a)(s.entity))?e.push(s):i.push(s)}),this.setProperties({_config:t,_entitiesDialog:e,_entitiesToggle:i})}_computeVisible(t,e){return t.filter(t=>t.entity in e)}_computeIcon(t,e){return Object(q.a)(e[t])}_computeButtonClass(t,e){return U.has(e[t].state)?"":"state-on"}_computeTooltip(t,e){return`${Object(g.a)(e[t])}: ${Object(y.a)(this.localize,e[t])}`}_computeImageClass(t){return t.navigation_path||t.camera_image?"clickable":""}_openDialog(t){this.fire("hass-more-info",{entityId:t.model.item.entity})}_callService(t){$(this.hass,t.model.item.entity)}_handleImageClick(){this._config.navigation_path?this.navigate(this._config.navigation_path):this._config.camera_image&&this.fire("hass-more-info",{entityId:this._config.camera_image})}}),i(170),customElements.define("hui-plant-status-card",class extends D{constructor(){super("ha-plant-card","plant")}}),customElements.define("hui-vertical-stack-card",class extends a.a{static get template(){return s["a"]`
      <style>
        #root {
          display: flex;
          flex-direction: column;
        }
        #root > * {
          margin: 4px 0 8px 0;
        }
        #root > *:first-child {
          margin-top: 0;
        }
        #root > *:last-child {
          margin-bottom: 0;
        }
      </style>
      <div id="root"></div>
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"}}}constructor(){super(),this._elements=[]}ready(){super.ready(),this._config&&this._buildConfig()}getCardSize(){let t=0;return this._elements.forEach(e=>{t+=z(e)}),t}setConfig(t){if(!t||!t.cards||!Array.isArray(t.cards))throw new Error("Card config incorrect");this._config=t,this.$&&this._buildConfig()}_buildConfig(){const t=this._config;this._elements=[];const e=this.$.root;for(;e.lastChild;)e.removeChild(e.lastChild);const i=[];t.cards.forEach(t=>{const s=G(t);s.hass=this.hass,i.push(s),e.appendChild(s)}),this._elements=i}_hassChanged(t){this._elements.forEach(e=>{e.hass=t})}}),i(174),customElements.define("hui-weather-forecast-card",class extends D{constructor(){super("ha-weather-card","weather")}getCardSize(){return 4}});const W=["entities","entity-filter","error","glance","history-graph","horizontal-stack","iframe","map","markdown","media-control","picture","picture-elements","picture-entity","picture-glance","plant-status","vertical-stack","weather-forecast"],J="custom:";function Z(t,e){const i=document.createElement(t);try{i.setConfig(e)}catch(i){return console.error(t,i),K(i.message,e)}return i}function K(t,e){return Z("hui-error-card",C(t,e))}function G(t){let e;if(!t||"object"!=typeof t||!t.type)return K("No card type configured.",t);if(t.type.startsWith(J)){if(e=t.type.substr(J.length),customElements.get(e))return Z(e,t);const i=K(`Custom element doesn't exist: ${e}.`,t);return customElements.whenDefined(e).then(()=>Object(l.a)(i,"rebuild-view")),i}return W.includes(t.type)?Z(`hui-${t.type}-card`,t):K(`Unknown card type encountered: ${t.type}.`,t)}customElements.define("hui-unused-entities",class extends a.a{static get template(){return s["a"]`
      <style>
        #root {
          max-width: 600px;
          margin: 0 auto;
          padding: 8px 0;
        }
      </style>
      <div id="root"></div>
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},config:{type:Object,observer:"_configChanged"}}}_configChanged(t){const e=this.$.root;e.lastChild&&e.removeChild(e.lastChild);const i=G({type:"entities",title:"Unused entities",entities:function(t,e){const i=function(t){const e=new Set;function i(t){e.add("string"==typeof t?t:t.entity)}return t.views.forEach(t=>(function t(e){e.entity&&i(e.entity),e.entities&&e.entities.forEach(t=>i(t)),e.card&&t(e.card),e.cards&&e.cards.forEach(e=>t(e))})(t)),e}(e);return Object.keys(t.states).filter(t=>!(i.has(t)||e.excluded_entities&&e.excluded_entities.includes(t)||c.includes(t.split(".",1)[0]))).sort()}(this.hass,t).map(t=>({entity:t,secondary_info:"entity-id"})),show_header_toggle:!1});i.hass=this.hass,e.appendChild(i)}_hassChanged(t){const e=this.$.root;e.lastChild&&(e.lastChild.hass=t)}});var Q=i(113);customElements.define("hui-view",class extends a.a{static get template(){return s["a"]`
      <style>
      :host {
        display: block;
        padding: 4px 4px 0;
        transform: translateZ(0);
        position: relative;
      }

      #badges {
        margin: 8px 16px;
        font-size: 85%;
        text-align: center;
      }

      #columns {
        display: flex;
        flex-direction: row;
        justify-content: center;
      }

      .column {
        flex-basis: 0;
        flex-grow: 1;
        max-width: 500px;
        overflow-x: hidden;
      }

      .column > * {
        display: block;
        margin: 4px 4px 8px;
      }

      @media (max-width: 500px) {
        :host {
          padding-left: 0;
          padding-right: 0;
        }

        .column > * {
          margin-left: 0;
          margin-right: 0;
        }
      }

      @media (max-width: 599px) {
        .column {
          max-width: 600px;
        }
      }
      </style>
      <div id="badges"></div>
      <div id="columns"></div>
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},config:Object,columns:Number}}static get observers(){return["_createBadges(config)","_createCards(config, columns)"]}constructor(){super(),this._cards=[],this._badges=[]}_createBadges(t){const e=this.$.badges;for(;e.lastChild;)e.removeChild(e.lastChild);if(!t||!t.badges||!Array.isArray(t.badges))return e.style.display="none",void(this._badges=[]);const i=[];for(const s of t.badges){if(!(s in this.hass.states))continue;const t=document.createElement("ha-state-label-badge");t.state=this.hass.states[s],i.push({element:t,entityId:s}),e.appendChild(t)}this._badges=i,e.style.display=i.length>0?"block":"none"}_createCards(t){const e=this.$.columns;for(;e.lastChild;)e.removeChild(e.lastChild);if(!t||!t.cards||!Array.isArray(t.cards))return void(this._cards=[]);const i=t.cards.map(t=>{const e=G(t);return e.hass=this.hass,e});let s=[];const a=[];for(let t=0;t<this.columns;t++)s.push([]),a.push(0);i.forEach(t=>{this.appendChild(t);const e="function"==typeof t.getCardSize?t.getCardSize():1;s[function(t){let e=0;for(let t=0;t<a.length;t++){if(a[t]<5){e=t;break}a[t]<a[e]&&(e=t)}return a[e]+=t,e}(e)].push(t)}),(s=s.filter(t=>t.length>0)).forEach(t=>{const i=document.createElement("div");i.classList.add("column"),t.forEach(t=>i.appendChild(t)),e.appendChild(i)}),this._cards=i,"theme"in t&&Object(Q.a)(e,this.hass.themes,t.theme)}_hassChanged(t){this._badges.forEach(e=>{const{element:i,entityId:s}=e;i.setProperties({hass:t,state:t.states[s]})}),this._cards.forEach(e=>{e.hass=t})}});const X={};customElements.define("hui-root",class extends(Object(r.a)(Object(n.a)(a.a))){static get template(){return s["a"]`
    <style include='ha-style'>
      :host {
        -ms-user-select: none;
        -webkit-user-select: none;
        -moz-user-select: none;
      }

      ha-app-layout {
        min-height: 100%;
      }
      paper-tabs {
        margin-left: 12px;
        --paper-tabs-selection-bar-color: var(--text-primary-color, #FFF);
        text-transform: uppercase;
      }
      app-toolbar a {
        color: var(--text-primary-color, white);
      }
      #view {
        min-height: calc(100vh - 112px);
        /**
         * Since we only set min-height, if child nodes need percentage
         * heights they must use absolute positioning so we need relative
         * positioning here.
         *
         * https://www.w3.org/TR/CSS2/visudet.html#the-height-property
         */
        position: relative;
      }
      #view.tabs-hidden {
        min-height: calc(100vh - 64px);
      }
      paper-item {
        cursor: pointer;
      }
    </style>
    <app-route route="[[route]]" pattern="/:view" data="{{routeData}}"></app-route>
    <ha-app-layout id="layout">
      <app-header slot="header" fixed>
        <app-toolbar>
          <ha-menu-button narrow='[[narrow]]' show-menu='[[showMenu]]'></ha-menu-button>
          <div main-title>[[_computeTitle(config)]]</div>
          <ha-start-voice-button hass="[[hass]]"></ha-start-voice-button>
          <paper-menu-button
            no-animations
            horizontal-align="right"
            horizontal-offset="-5"
          >
            <paper-icon-button icon="hass:dots-vertical" slot="dropdown-trigger"></paper-icon-button>
            <paper-listbox on-iron-select="_deselect" slot="dropdown-content">
              <paper-item on-click="_handleRefresh">Refresh</paper-item>
              <paper-item on-click="_handleUnusedEntities">Unused entities</paper-item>
              <paper-item on-click="_handleHelp">Help</paper-item>
            </paper-listbox>
          </paper-menu-button>
        </app-toolbar>

        <div sticky hidden$="[[_computeTabsHidden(config.views)]]">
          <paper-tabs scrollable selected="[[_curView]]" on-iron-activate="_handleViewSelected">
            <template is="dom-repeat" items="[[config.views]]">
              <paper-tab>
                <template is="dom-if" if="[[item.icon]]">
                  <ha-icon title$="[[item.title]]" icon="[[item.icon]]"></ha-icon>
                </template>
                <template is="dom-if" if="[[!item.icon]]">
                  [[_computeTabTitle(item.title)]]
                </template>
              </paper-tab>
            </template>
          </paper-tabs>
        </div>
      </app-header>

      <div id='view' on-rebuild-view='_debouncedConfigChanged'></div>
    </app-header-layout>
    `}static get properties(){return{narrow:Boolean,showMenu:Boolean,hass:{type:Object,observer:"_hassChanged"},config:{type:Object,observer:"_configChanged"},columns:{type:Number,observer:"_columnsChanged"},_curView:{type:Number,value:0},route:{type:Object,observer:"_routeChanged"},routeData:Object}}constructor(){super(),this._debouncedConfigChanged=N(()=>this._selectView(this._curView),100)}_routeChanged(t){const e=this.config&&this.config.views;if(""===t.path&&"/lovelace"===t.prefix&&e)this.navigate(`/lovelace/${e[0].id||0}`,!0);else if(this.routeData.view){const t=this.routeData.view;let i=0;for(let s=0;s<e.length;s++)if(e[s].id===t||s===parseInt(t)){i=s;break}i!==this._curView&&this._selectView(i)}}_computeViewId(t,e){return t||e}_computeTitle(t){return t.title||"Home Assistant"}_computeTabsHidden(t){return t.length<2}_computeTabTitle(t){return t||"Unnamed view"}_handleRefresh(){this.fire("config-refresh")}_handleUnusedEntities(){this._selectView("unused")}_deselect(t){t.target.selected=null}_handleHelp(){window.open("https://www.home-assistant.io/lovelace/","_blank")}_handleViewSelected(t){const e=t.detail.selected;if(e!==this._curView){const t=this.config.views[e].id||e;this.navigate(`/lovelace/${t}`)}var i,s,a,n,r,o,c;i=this,s=this.$.layout.header.scrollTarget,a=s,n=Math.random(),r=Date.now(),o=a.scrollTop,c=0-o,i._currentAnimationId=n,function t(){var e,s=Date.now()-r;s>200?a.scrollTop=0:i._currentAnimationId===n&&(a.scrollTop=(e=s,-c*(e/=200)*(e-2)+o),requestAnimationFrame(t.bind(i)))}.call(i)}_selectView(t){this._curView=t;const e=this.$.view;let i;e.lastChild&&e.removeChild(e.lastChild);let s=this.config.background||"";if("unused"===t)(i=document.createElement("hui-unused-entities")).config=this.config;else{const t=this.config.views[this._curView];t.panel?(i=G(t.cards[0])).isPanel=!0:((i=document.createElement("hui-view")).config=t,i.columns=this.columns),t.background&&(s=t.background)}this.$.view.style.background=s,i.hass=this.hass,e.appendChild(i)}_hassChanged(t){this.$.view.lastChild&&(this.$.view.lastChild.hass=t)}_configChanged(t){this._loadResources(t.resources||[]),this._selectView(this._curView),this.$.view.classList.toggle("tabs-hidden",t.views.length<2)}_columnsChanged(t){this.$.view.lastChild&&(this.$.view.lastChild.columns=t)}_loadResources(t){t.forEach(t=>{switch(t.type){case"js":if(t.url in X)break;X[t.url]=Object(o.a)(t.url);break;case"module":Object(o.b)(t.url);break;case"html":Promise.resolve().then(i.bind(null,158)).then(({importHref:e})=>e(t.url));break;default:console.warn("Unknown resource type specified: ${resource.type}")}})}}),customElements.define("ha-panel-lovelace",class extends a.a{static get template(){return s["a"]`
      <style>
        paper-button {
          color: var(--primary-color);
          font-weight: 500;
        }
      </style>
      <template is='dom-if' if='[[_equal(_state, "loaded")]]' restamp>
        <hui-root
          narrow="[[narrow]]"
          show-menu="[[showMenu]]"
          hass='[[hass]]'
          route="[[route]]"
          config='[[_config]]'
          columns='[[_columns]]'
          on-config-refresh='_fetchConfig'
        ></hui-root>
      </template>
      <template is='dom-if' if='[[_equal(_state, "loading")]]' restamp>
        <hass-loading-screen
          narrow="[[narrow]]"
          show-menu="[[showMenu]]"
        ></hass-loading-screen>
      </template>
      <template is='dom-if' if='[[_equal(_state, "error")]]' restamp>
        <hass-error-screen
          title='Lovelace'
          error='[[_errorMsg]]'
          narrow="[[narrow]]"
          show-menu="[[showMenu]]"
        >
          <paper-button on-click="_fetchConfig">Reload ui-lovelace.yaml</paper-button>
        </hass-error-screen>
      </template>
    `}static get properties(){return{hass:Object,narrow:{type:Boolean,value:!1},showMenu:{type:Boolean,value:!1},route:Object,_columns:{type:Number,value:1},_state:{type:String,value:"loading"},_errorMsg:String,_config:{type:Object,value:null}}}static get observers(){return["_updateColumns(narrow, showMenu)"]}ready(){this._fetchConfig(),this._updateColumns=this._updateColumns.bind(this),this.mqls=[300,600,900,1200].map(t=>{const e=matchMedia(`(min-width: ${t}px)`);return e.addListener(this._updateColumns),e}),this._updateColumns(),super.ready()}_updateColumns(){const t=this.mqls.reduce((t,e)=>t+e.matches,0);this._columns=Math.max(1,t-(!this.narrow&&this.showMenu))}async _fetchConfig(){try{const t=await this.hass.callWS({type:"frontend/lovelace_config"});this.setProperties({_config:t,_state:"loaded"})}catch(t){this.setProperties({_state:"error",_errorMsg:t.message})}}_equal(t,e){return t===e}})},76:function(t,e,i){"use strict";function s(t,e,i){return new Promise(function(s,a){const n=document.createElement(t);let r="src",o="body";switch(n.onload=(()=>s(e)),n.onerror=(()=>a(e)),t){case"script":n.async=!0,i&&(n.type=i);break;case"link":n.type="text/css",n.rel="stylesheet",r="href",o="head"}n[r]=e,document[o].appendChild(n)})}i.d(e,"a",function(){return a}),i.d(e,"b",function(){return n});const a=t=>s("script",t),n=t=>s("script",t,"module")}}]);
//# sourceMappingURL=c5a5df3ec278008029fa.chunk.js.map