(window.webpackJsonp=window.webpackJsonp||[]).push([[20],{202:function(e,t,i){"use strict";var s=i(0),a=i(3),n=(i(210),i(15));customElements.define("ha-call-service-button",class extends(Object(n.a)(a.a)){static get template(){return s["a"]`
    <ha-progress-button id="progress" progress="[[progress]]" on-click="buttonTapped"><slot></slot></ha-progress-button>
`}static get properties(){return{hass:{type:Object},progress:{type:Boolean,value:!1},domain:{type:String},service:{type:String},serviceData:{type:Object,value:{}}}}buttonTapped(){this.progress=!0;var e=this,t={domain:this.domain,service:this.service,serviceData:this.serviceData};this.hass.callService(this.domain,this.service,this.serviceData).then(function(){e.progress=!1,e.$.progress.actionSuccess(),t.success=!0},function(){e.progress=!1,e.$.progress.actionError(),t.success=!1}).then(function(){e.fire("hass-service-called",t)})}})},210:function(e,t,i){"use strict";i(60),i(128);var s=i(0),a=i(3);customElements.define("ha-progress-button",class extends a.a{static get template(){return s["a"]`
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
`}static get properties(){return{hass:{type:Object},progress:{type:Boolean,value:!1},disabled:{type:Boolean,value:!1}}}tempClass(e){var t=this.$.container.classList;t.add(e),setTimeout(()=>{t.remove(e)},1e3)}ready(){super.ready(),this.addEventListener("click",e=>this.buttonTapped(e))}buttonTapped(e){this.progress&&e.stopPropagation()}actionSuccess(){this.tempClass("success")}actionError(){this.tempClass("error")}computeDisabled(e,t){return e||t}})},301:function(e,t,i){"use strict";i.d(t,"a",function(){return n});var s=i(260),a=i.n(s);function n(e){const t=a.a.map(e),i=document.createElement("link");return i.setAttribute("href","/static/images/leaflet/leaflet.css"),i.setAttribute("rel","stylesheet"),e.parentNode.appendChild(i),t.setView([51.505,-.09],13),a.a.tileLayer(`https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}${a.a.Browser.retina?"@2x.png":".png"}`,{attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',subdomains:"abcd",minZoom:0,maxZoom:20}).addTo(t),t}},302:function(e,t,i){"use strict";i(164);var s=i(0),a=i(3),n=i(15);customElements.define("ha-entity-marker",class extends(Object(n.a)(a.a)){static get template(){return s["a"]`
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
`}static get properties(){return{hass:{type:Object},entityId:{type:String,value:""},entityName:{type:String,value:null},entityPicture:{type:String,value:null}}}ready(){super.ready(),this.addEventListener("click",e=>this.badgeTap(e))}badgeTap(e){e.stopPropagation(),this.entityId&&this.fire("hass-more-info",{entityId:this.entityId})}})},599:function(e,t,i){"use strict";i.r(t);var s=i(0),a=i(3);i(60),i(168),i(162),i(151),i(150),i(116),i(103),i(59),i(101),i(115),i(118),i(138),i(166);var n=i(15),r=i(75),o=(i(153),i(163),i(88),i(76));const c=["group","zone"];var l=i(98);function h(e){if(!e||!Array.isArray(e))throw new Error("Entities need to be an array");return e.map((e,i)=>{if("string"==typeof e)e={entity:e};else{if("object"!=typeof e||Array.isArray(e))throw new Error(`Invalid entity specified at position ${i}.`);if(!e.entity)throw new Error(`Entity object at position ${i} is missing entity field.`)}if(t=e.entity,!/^(\w+)\.(\w+)$/.test(t))throw new Error(`Invalid entity ID at position ${i}: ${e.entity}`);return e});var t}i(30),i(102),i(156);var d=i(109),p=i(36),u=i(66);const m=["cover","lock"];customElements.define("hui-entities-toggle",class extends a.a{static get template(){return s["a"]`
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
`}static get properties(){return{hass:Object,entities:Array,_toggleEntities:{type:Array,computed:"_computeToggleEntities(hass, entities)"}}}_computeToggleEntities(e,t){return t.filter(t=>t in e.states&&!m.includes(t.split(".",1)[0])&&Object(d.a)(e,e.states[t]))}_computeIsChecked(e,t){return t.some(t=>!p.g.includes(e.states[t].state))}_callService(e){const t=e.target.checked;!function(e,t,i=!0){const s={};t.forEach(t=>{if(p.g.includes(e.states[t].state)===i){const e=Object(u.a)(t),i=["cover","lock"].includes(e)?e:"homeassistant";i in s||(s[i]=[]),s[i].push(t)}}),Object.keys(s).forEach(t=>{let a;switch(t){case"lock":a=i?"unlock":"lock";break;case"cover":a=i?"open_cover":"close_cover";break;default:a=i?"turn_on":"turn_off"}const n=s[t];e.callService(t,a,{entity_id:n})})}(this.hass,this._toggleEntities,t)}}),i(159);var g=i(140);function f(e,t){return{type:"error",error:e,origConfig:t}}const _="custom:";function b(e,t,i,s){const a=document.createElement(e);try{"setConfig"in a&&a.setConfig(t)}catch(i){return console.error(e,i),y(i.message,t)}return a.stateObj=i,a.hass=s,t.name&&(a.overrideName=t.name),a}function y(e,t){return b("hui-error-card",f(e,t))}function v(e,t){let i;if(!e||"object"!=typeof e)return y("Invalid config given.",e);const s=e.entity;if(!(s in t.states))return y("Entity not found.",e);const a=e.type||"default",n=t.states[s];if(a.startsWith(_)){if(i=a.substr(_.length),customElements.get(i))return b(i,e,n,t);const s=y(`Custom element doesn't exist: ${i}.`,e);return customElements.whenDefined(i).then(()=>Object(l.a)(s,"rebuild-view")),s}return b(i=n?`state-card-${Object(g.a)(t,n)}`:"state-card-display",e,n,t)}customElements.define("hui-entities-card",class extends(Object(n.a)(a.a)){static get template(){return s["a"]`
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
`}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},_config:Object}}constructor(){super(),this._elements=[]}ready(){super.ready(),this._config&&this._buildConfig()}getCardSize(){return 1+(this._config?this._config.entities.length:0)}_showHeaderToggle(e){return!1!==e}_showHeader(e){return e.title||e.show_header_toggle}setConfig(e){this._config=e,this._configEntities=h(e.entities),this.$&&this._buildConfig()}_buildConfig(){const e=this.$.states,t=this._configEntities;for(;e.lastChild;)e.removeChild(e.lastChild);this._elements=[];for(const i of t){const t=i.entity,s=v(i,this.hass);t&&!p.c.includes(Object(u.a)(t))&&(s.classList.add("state-card-dialog"),s.addEventListener("click",()=>this.fire("hass-more-info",{entityId:t}))),this._elements.push({entityId:t,element:s});const a=document.createElement("div");a.appendChild(s),e.appendChild(a)}}_hassChanged(e){for(let t=0;t<this._elements.length;t++){const{entityId:i,element:s}=this._elements[t],a=e.states[i];s.stateObj=a,s.hass=e}}}),customElements.define("hui-entity-filter-card",class extends a.a{static get properties(){return{hass:{type:Object,observer:"_hassChanged"}}}getCardSize(){return this.lastChild?this.lastChild.getCardSize():1}setConfig(e){if(!e.state_filter||!Array.isArray(e.state_filter))throw new Error("Incorrect filter config.");this._config=e,this._configEntities=h(e.entities),this.lastChild&&(this.removeChild(this.lastChild),this._element=null);const t="card"in e?Object.assign({},e.card):{};t.type||(t.type="entities"),t.entities=[];const i=B(t);i._filterRawConfig=t,this._updateCardConfig(i),this._element=i}_hassChanged(){this._updateCardConfig(this._element)}_updateCardConfig(e){if(!e||"HUI-ERROR-CARD"===e.tagName||!this.hass)return;const t=(i=this.hass,s=this._config.state_filter,this._configEntities.filter(e=>{const t=i.states[e.entity];return t&&s.includes(t.state)}));var i,s;0!==t.length||!1!==this._config.show_empty?(this.style.display="block",e.setConfig(Object.assign({},e._filterRawConfig,{entities:t})),e.isPanel=this.isPanel,e.hass=this.hass,this.lastChild||this.appendChild(e)):this.style.display="none"}}),customElements.define("hui-error-card",class extends a.a{static get template(){return s["a"]`
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
    `}static get properties(){return{_config:Object}}setConfig(e){this._config=e}getCardSize(){return 4}_toStr(e){return JSON.stringify(e,null,2)}});var w=i(105),C=i(28);function k(e,t,i=!0){const s=Object(u.a)(t),a="group"===s?"homeassistant":s;let n;switch(s){case"lock":n=i?"unlock":"lock";break;case"cover":n=i?"open_cover":"close_cover";break;default:n=i?"turn_on":"turn_off"}e.callService(a,n,{entity_id:t})}function E(e,t){k(e,t,p.g.includes(e.states[t].state))}i(119);var x=i(13);function j(e){return"function"==typeof e.getCardSize?e.getCardSize():1}customElements.define("hui-glance-card",class extends(Object(x.a)(Object(n.a)(a.a))){static get template(){return s["a"]`
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
    `}static get properties(){return{hass:Object,_config:Object,_configEntities:Array}}getCardSize(){return 3}setConfig(e){this._config=e,this.updateStyles({"--glance-column-width":e&&e.column_width||"20%"}),this._configEntities=h(e.entities)}_showEntity(e,t){return e.entity in t}_showInfo(e){return!1!==e}_computeName(e,t){return e.name||Object(C.a)(t[e.entity])}_computeStateObj(e,t){return t[e.entity]}_computeState(e,t){return Object(w.a)(this.localize,t[e.entity])}_handleClick(e){const t=e.model.item.entity;switch(e.model.item.tap_action){case"toggle":E(this.hass,t);break;case"turn-on":k(this.hass,t,!0);break;default:this.fire("hass-more-info",{entityId:t})}}}),i(158),i(160),customElements.define("hui-history-graph-card",class extends a.a{static get template(){return s["a"]`
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
    `}static get properties(){return{hass:Object,_config:Object,stateHistory:{type:Object},_names:Array,_entities:Object,stateHistoryLoading:Boolean}}getCardSize(){return 4}setConfig(e){const t=h(e.entities);this._config=e;const i=[],s={};for(const e of t)i.push(e.entity),e.name&&(s[e.entity]=e.name);this._entities=i,this._names=s}_computeCacheConfig(e){return{cacheKey:e.entities,hoursToShow:e.hours_to_show||24,refresh:e.refresh_interval||0}}}),customElements.define("hui-horizontal-stack-card",class extends a.a{static get template(){return s["a"]`
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
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"}}}constructor(){super(),this._elements=[]}ready(){super.ready(),this._config&&this._buildConfig()}getCardSize(){let e=1;return this._elements.forEach(t=>{const i=j(t);i>e&&(e=i)}),e}setConfig(e){if(!e||!e.cards||!Array.isArray(e.cards))throw new Error("Card config incorrect.");this._config=e,this.$&&this._buildConfig()}_buildConfig(){const e=this._config;this._elements=[];const t=this.$.root;for(;t.lastChild;)t.removeChild(t.lastChild);const i=[];e.cards.forEach(e=>{const s=B(e);s.hass=this.hass,i.push(s),t.appendChild(s)}),this._elements=i}_hassChanged(e){this._elements.forEach(t=>{t.hass=e})}}),customElements.define("hui-iframe-card",class extends a.a{static get template(){return s["a"]`
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
    `}static get properties(){return{_config:Object}}ready(){super.ready(),this._config&&this._buildConfig()}setConfig(e){this._config=e,this.$&&this._buildConfig()}_buildConfig(){const e=this._config;this.$.root.style.paddingTop=e.aspect_ratio||"50%"}getCardSize(){return 1+this.offsetHeight/50}});var O=i(260),I=i.n(O),S=(i(302),i(301)),$=i(25);function z(e,t,i){let s;return function(...a){const n=this,r=i&&!s;clearTimeout(s),s=setTimeout(()=>{s=null,i||e.apply(n,a)},t),r&&e.apply(n,a)}}I.a.Icon.Default.imagePath="/static/images/leaflet",customElements.define("hui-map-card",class extends a.a{static get template(){return s["a"]`
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

    `}static get properties(){return{hass:{type:Object,observer:"_drawEntities"},_config:Object,isPanel:{type:Boolean,reflectToAttribute:!0}}}constructor(){super(),this._debouncedResizeListener=z(this._resetMap.bind(this),100)}ready(){super.ready(),this._config&&!this.isPanel&&(this.$.root.style.paddingTop=this._config.aspect_ratio||"100%")}setConfig(e){if(!e)throw new Error("Error in card configuration.");this._configEntities=h(e.entities),this._config=e}getCardSize(){let e=this._config.aspect_ratio||"100%";return e=e.substr(0,e.length-1),1+Math.floor(e/25)||3}connectedCallback(){super.connectedCallback(),"function"==typeof ResizeObserver?(this._resizeObserver=new ResizeObserver(()=>this._debouncedResizeListener()),this._resizeObserver.observe(this.$.map)):window.addEventListener("resize",this._debouncedResizeListener),this._map=Object(S.a)(this.$.map),this._drawEntities(this.hass),setTimeout(()=>{this._resetMap(),this._fitMap()},1)}disconnectedCallback(){super.disconnectedCallback(),this._map&&this._map.remove(),this._resizeObserver?this._resizeObserver.unobserve(this.$.map):window.removeEventListener("resize",this._debouncedResizeListener)}_resetMap(){this._map&&this._map.invalidateSize()}_fitMap(){if(0===this._mapItems.length)this._map.setView(new I.a.LatLng(this.hass.config.core.latitude,this.hass.config.core.longitude),14);else{const e=new I.a.latLngBounds(this._mapItems.map(e=>e.getLatLng()));this._map.fitBounds(e.pad(.5))}}_drawEntities(e){const t=this._map;if(!t)return;this._mapItems&&this._mapItems.forEach(e=>e.remove());const i=this._mapItems=[];this._configEntities.forEach(s=>{const a=s.entity;if(!(a in e.states))return;const n=e.states[a],r=Object(C.a)(n),{latitude:o,longitude:c,passive:l,icon:h,radius:d,entity_picture:p,gps_accuracy:u}=n.attributes;if(!o||!c)return;let m,g,f;if("zone"===Object($.a)(n)){if(l)return;return h?((f=document.createElement("ha-icon")).setAttribute("icon",h),g=f.outerHTML):g=r,m=I.a.divIcon({html:g,iconSize:[24,24],className:""}),i.push(I.a.marker([o,c],{icon:m,interactive:!1,title:r}).addTo(t)),void i.push(I.a.circle([o,c],{interactive:!1,color:"#FF9800",radius:d}).addTo(t))}const _=r.split(" ").map(e=>e[0]).join("").substr(0,3);(f=document.createElement("ha-entity-marker")).setAttribute("entity-id",a),f.setAttribute("entity-name",_),f.setAttribute("entity-picture",p||""),m=I.a.divIcon({html:f.outerHTML,iconSize:[48,48],className:""}),i.push(I.a.marker([o,c],{icon:m,title:Object(C.a)(n)}).addTo(t)),u&&i.push(I.a.circle([o,c],{interactive:!1,color:"#0288D1",radius:u}).addTo(t))})}}),i(155),customElements.define("hui-markdown-card",class extends a.a{static get template(){return s["a"]`
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
    `}static get properties(){return{_config:Object,noTitle:{type:Boolean,reflectToAttribute:!0,computed:"_computeNoTitle(_config.title)"}}}setConfig(e){this._config=e}getCardSize(){return this._config.content.split("\n").length}_computeNoTitle(e){return!e}}),i(170);class T extends HTMLElement{constructor(e,t){super(),this._tag=e.toUpperCase(),this._domain=t,this._element=null}getCardSize(){return 3}setConfig(e){if(!e.entity)throw new Error("No entity specified");if(Object(u.a)(e.entity)!==this._domain)throw new Error(`Specified entity needs to be of domain ${this._domain}.`);this._config=e}set hass(e){const t=this._config.entity;t in e.states?(this._ensureElement(this._tag),this.lastChild.hass=e,this.lastChild.stateObj=e.states[t]):(this._ensureElement("HUI-ERROR-CARD"),this.lastChild.setConfig(f(`No state available for ${t}`,this._config)))}_ensureElement(e){this.lastChild&&this.lastChild.tagName===e||(this.lastChild&&this.removeChild(this.lastChild),this.appendChild(document.createElement(e)))}}customElements.define("hui-media-control-card",class extends T{constructor(){super("ha-media_player-card","media_player")}}),customElements.define("hui-picture-card",class extends(Object(r.a)(a.a)){static get template(){return s["a"]`
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
    `}static get properties(){return{hass:Object,_config:Object}}getCardSize(){return 3}setConfig(e){if(!e||!e.image)throw new Error("Error in card configuration.");this._config=e}_computeClickable(e){return e.navigation_path||e.service}_cardClicked(){if(this._config.navigation_path&&this.navigate(this._config.navigation_path),this._config.service){const[e,t]=this._config.service.split(".",2);this.hass.callService(e,t,this._config.service_data)}}}),i(202),i(165);customElements.define("hui-image",class extends(Object(x.a)(a.a)){static get template(){return s["a"]`
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
`}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},entity:String,image:String,stateImage:Object,cameraImage:String,filter:String,stateFilter:Object,_imageSrc:String}}static get observers(){return["_configChanged(image, stateImage, cameraImage)"]}connectedCallback(){super.connectedCallback(),this.cameraImage&&(this.timer=setInterval(()=>this._updateCameraImageSrc(),1e4))}disconnectedCallback(){super.disconnectedCallback(),clearInterval(this.timer)}_configChanged(e,t,i){i?this._updateCameraImageSrc():e&&!t&&(this._imageSrc=e)}_onImageError(){this._imageSrc=null,this.$.image.classList.add("hidden"),this.$.brokenImage.style.setProperty("height",`${this._lastImageHeight||"100"}px`),this.$.brokenImage.classList.remove("hidden")}_onImageLoad(){this.$.image.classList.remove("hidden"),this.$.brokenImage.classList.add("hidden"),this._lastImageHeight=this.$.image.offsetHeight}_hassChanged(e){if(this.cameraImage||!this.entity)return;const t=e.states[this.entity],i=t?t.state:"unavailable";i!==this._currentState&&(this._currentState=i,this._updateStateImage(),this._updateStateFilter(t))}_updateStateImage(){if(!this.stateImage)return void(this._imageFallback=!0);const e=this.stateImage[this._currentState];this._imageSrc=e||this.image,this._imageFallback=!e}_updateStateFilter(e){let t;t=this.stateFilter&&this.stateFilter[this._currentState]||this.filter;const i=!e||p.g.includes(e.state);this.$.image.style.filter=t||i&&this._imageFallback&&"grayscale(100%)"||""}_updateCameraImageSrc(){this.hass.connection.sendMessagePromise({type:"camera_thumbnail",entity_id:this.cameraImage}).then(e=>{e.success?(this._imageSrc=`data:${e.result.content_type};base64, ${e.result.content}`,this._onImageLoad()):this._onImageError()},()=>this._onImageError())}});const L=new Set(["image","navigation","service-button","service-icon","state-badge","state-icon","state-label"]);customElements.define("hui-picture-elements-card",class extends(Object(r.a)(Object(n.a)(Object(x.a)(a.a)))){static get template(){return s["a"]`
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
      .state-label {
        padding: 8px;
        white-space: nowrap;
      }
      .clickable {
        cursor: pointer;
      }
      ha-call-service-button {
        color: var(--primary-color);
        white-space: nowrap;
      }
      hui-image {
        overflow-y: hidden;
      }
    </style>

    <ha-card header="[[_config.title]]">
      <div id="root"></div>
    </ha-card>
`}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},_config:Object}}constructor(){super(),this._stateBadges=[],this._stateIcons=[],this._stateLabels=[],this._images=[]}ready(){super.ready(),this._config&&this._buildConfig()}getCardSize(){return 4}setConfig(e){if(!e||!e.image||!Array.isArray(e.elements))throw new Error("Invalid card configuration");const t=e.elements.map(e=>e.type).filter(e=>!L.has(e));if(t.length)throw new Error(`Incorrect element types: ${t.join(", ")}`);this._config=e,this.$&&this._buildConfig()}_buildConfig(){const e=this._config,t=this.$.root;for(this._stateBadges=[],this._stateIcons=[],this._stateLabels=[];t.lastChild;)t.removeChild(t.lastChild);const i=document.createElement("img");i.src=e.image,t.appendChild(i),e.elements.forEach(e=>{const i=e.entity;let s;switch(e.type){case"service-button":s=document.createElement("ha-call-service-button"),[s.domain,s.service]=e.service.split(".",2),s.serviceData=e.service_data||{},s.innerText=e.title,s.hass=this.hass;break;case"service-icon":(s=document.createElement("ha-icon")).icon=e.icon,s.title=e.title||"",s.addEventListener("click",()=>this._handleClick(e)),s.classList.add("clickable");break;case"state-badge":(s=document.createElement("ha-state-label-badge")).state=this.hass.states[i],this._stateBadges.push({el:s,entityId:i});break;case"state-icon":(s=document.createElement("state-badge")).addEventListener("click",()=>this._handleClick(e)),s.classList.add("clickable"),this._stateIcons.push({el:s,entityId:i});break;case"state-label":(s=document.createElement("div")).addEventListener("click",()=>this._handleClick(e)),s.classList.add("clickable","state-label"),this._stateLabels.push({el:s,entityId:i});break;case"navigation":(s=document.createElement("ha-icon")).icon=e.icon||"hass:image-filter-center-focus",s.addEventListener("click",()=>this.navigate(e.navigation_path)),s.title=e.navigation_path,s.classList.add("clickable");break;case"image":if((s=document.createElement("hui-image")).hass=this.hass,s.entity=e.entity,s.image=e.image,s.stateImage=e.state_image,s.filter=e.filter,s.stateFilter=e.state_filter,e.camera_image||"camera"!==Object(u.a)(e.entity)?s.cameraImage=e.camera_image:s.cameraImage=e.entity,this._images.push(s),"none"===e.tap_action)break;s.addEventListener("click",()=>this._handleClick(e)),s.classList.add("clickable")}s.classList.add("element"),Object.keys(e.style).forEach(t=>{s.style.setProperty(t,e.style[t])}),t.appendChild(s)}),this.hass&&this._hassChanged(this.hass)}_hassChanged(e){this._stateBadges.forEach(t=>{const{el:i,entityId:s}=t;i.state=e.states[s],i.hass=e}),this._stateIcons.forEach(t=>{const{el:i,entityId:s}=t,a=e.states[s];a&&(i.stateObj=a,i.title=this._computeTooltip(a))}),this._stateLabels.forEach(t=>{const{el:i,entityId:s}=t,a=e.states[s];a?(i.innerText=Object(w.a)(this.localize,a),i.title=this._computeTooltip(a)):(i.innerText="N/A",i.title="")}),this._images.forEach(t=>{t.hass=e})}_computeTooltip(e){return`${Object(C.a)(e)}: ${Object(w.a)(this.localize,e)}`}_handleClick(e){switch(e.tap_action||("service-icon"===e.type?"call-service":"more-info")){case"more-info":this.fire("hass-more-info",{entityId:e.entity});break;case"toggle":E(this.hass,e.entity);break;case"call-service":{const[t,i]=e.service.split(".",2),s=Object.assign({},{entity_id:e.entity},e.service_data);this.hass.callService(t,i,s)}}}});customElements.define("hui-picture-entity-card",class extends(Object(n.a)(Object(x.a)(a.a))){static get template(){return s["a"]`
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
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},_config:Object}}getCardSize(){return 3}setConfig(e){if(!e||!e.entity)throw new Error("Error in card configuration.");if(this._entityDomain=Object(u.a)(e.entity),"camera"!==this._entityDomain&&!e.image&&!e.state_image&&!e.camera_image)throw new Error("No image source configured.");this._config=e}_hassChanged(e){const t=this._config,i=t.entity,s=e.states[i];if(!s&&"Unavailable"===this._oldState||s&&s.state===this._oldState)return;let a,n,r,o=!0;s?(a=t.name||Object(C.a)(s),n=s.state,r=this._computeStateLabel(s)):(a=t.name||i,n="Unavailable",r="Unavailable",o=!1),this.$.name.innerText=a,this.$.state.innerText=r,this._oldState=n,this.$.card.classList.toggle("canInteract",o)}_computeStateLabel(e){switch(this._entityDomain){case"scene":return this.localize("ui.card.scene.activate");case"script":return this.localize("ui.card.script.execute");case"weblink":return"Open";default:return Object(w.a)(this.localize,e)}}_computeHideInfo(e){return!1===e.show_info}_cardClicked(){const e=this._config&&this._config.entity;e&&e in this.hass.states&&("toggle"===this._config.tap_action?"weblink"===this._entityDomain?window.open(this.hass.states[e].state):E(this.hass,e):this.fire("hass-more-info",{entityId:e}))}_getCameraImage(e){return"camera"===this._entityDomain?e.entity:e.camera_image}});var A=i(110);const D=new Set(["input_boolean","light","switch"]);customElements.define("hui-picture-glance-card",class extends(Object(r.a)(Object(x.a)(Object(n.a)(a.a)))){static get template(){return s["a"]`
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
          <div class="title">[[_config.title]]</div>
          <div>
            <template is="dom-repeat" items="[[_entitiesDialog]]">
              <template is="dom-if" if="[[_showEntity(item.entity, hass.states)]]">
                <paper-icon-button
                  on-click="_openDialog"
                  class$="[[_computeButtonClass(item.entity, hass.states)]]"
                  icon="[[_computeIcon(item.entity, hass.states)]]"
                  title="[[_computeTooltip(item.entity, hass.states)]]"
                ></paper-icon-button>
              </template>
            </template>
          </div>
          <div>
            <template is="dom-repeat" items="[[_entitiesToggle]]">
              <template is="dom-if" if="[[_showEntity(item.entity, hass.states)]]">
                <paper-icon-button
                  on-click="_callService"
                  class$="[[_computeButtonClass(item.entity, hass.states)]]"
                  icon="[[_computeIcon(item.entity, hass.states)]]"
                  title="[[_computeTooltip(item.entity, hass.states)]]"
                ></paper-icon-button>
              </template>
            </template>
          </div>
        </div>
      </ha-card>
    `}static get properties(){return{hass:Object,_config:Object,_entitiesDialog:Array,_entitiesToggle:Array}}getCardSize(){return 3}setConfig(e){if(!e||!e.entities||!Array.isArray(e.entities)||!(e.image||e.camera_image||e.state_image)||e.state_image&&!e.entity)throw new Error("Invalid card configuration");const t=[],i=[];h(e.entities).forEach(s=>{e.force_dialog||!D.has(Object(u.a)(s.entity))?t.push(s):i.push(s)}),this.setProperties({_config:e,_entitiesDialog:t,_entitiesToggle:i})}_showEntity(e,t){return e in t}_computeIcon(e,t){return Object(A.a)(t[e])}_computeButtonClass(e,t){return p.g.includes(t[e].state)?"":"state-on"}_computeTooltip(e,t){return`${Object(C.a)(t[e])}: ${Object(w.a)(this.localize,t[e])}`}_computeImageClass(e){return e.navigation_path||e.camera_image?"clickable":""}_openDialog(e){this.fire("hass-more-info",{entityId:e.model.item.entity})}_callService(e){E(this.hass,e.model.item.entity)}_handleImageClick(){this._config.navigation_path?this.navigate(this._config.navigation_path):this._config.camera_image&&this.fire("hass-more-info",{entityId:this._config.camera_image})}}),i(169),customElements.define("hui-plant-status-card",class extends T{constructor(){super("ha-plant-card","plant")}}),customElements.define("hui-vertical-stack-card",class extends a.a{static get template(){return s["a"]`
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
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"}}}constructor(){super(),this._elements=[]}ready(){super.ready(),this._config&&this._buildConfig()}getCardSize(){let e=0;return this._elements.forEach(t=>{e+=j(t)}),e}setConfig(e){if(!e||!e.cards||!Array.isArray(e.cards))throw new Error("Card config incorrect");this._config=e,this.$&&this._buildConfig()}_buildConfig(){const e=this._config;this._elements=[];const t=this.$.root;for(;t.lastChild;)t.removeChild(t.lastChild);const i=[];e.cards.forEach(e=>{const s=B(e);s.hass=this.hass,i.push(s),t.appendChild(s)}),this._elements=i}_hassChanged(e){this._elements.forEach(t=>{t.hass=e})}}),i(173),customElements.define("hui-weather-forecast-card",class extends T{constructor(){super("ha-weather-card","weather")}getCardSize(){return 4}});const H=["entities","entity-filter","error","glance","history-graph","horizontal-stack","iframe","map","markdown","media-control","picture","picture-elements","picture-entity","picture-glance","plant-status","vertical-stack","weather-forecast"],M="custom:";function R(e,t){const i=document.createElement(e);try{i.setConfig(t)}catch(i){return console.error(e,i),N(i.message,t)}return i}function N(e,t){return R("hui-error-card",f(e,t))}function B(e){let t;if(!e||"object"!=typeof e||!e.type)return N("No card type configured.",e);if(e.type.startsWith(M)){if(t=e.type.substr(M.length),customElements.get(t))return R(t,e);const i=N(`Custom element doesn't exist: ${t}.`,e);return customElements.whenDefined(t).then(()=>Object(l.a)(i,"rebuild-view")),i}return H.includes(e.type)?R(`hui-${e.type}-card`,e):N(`Unknown card type encountered: ${e.type}.`,e)}customElements.define("hui-unused-entities",class extends a.a{static get template(){return s["a"]`
      <style>
        #root {
          max-width: 600px;
          margin: 0 auto;
          padding: 8px 0;
        }
      </style>
      <div id="root"></div>
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},config:{type:Object,observer:"_configChanged"}}}_configChanged(e){const t=this.$.root;t.lastChild&&t.removeChild(t.lastChild);const i=B({type:"entities",title:"Unused entities",entities:function(e,t){const i=function(e){const t=new Set;function i(e){t.add("string"==typeof e?e:e.entity)}return e.views.forEach(e=>(function e(t){t.entity&&i(t.entity),t.entities&&t.entities.forEach(e=>i(e)),t.card&&e(t.card),t.cards&&t.cards.forEach(t=>e(t))})(e)),t}(t);return Object.keys(e.states).filter(e=>!(i.has(e)||t.excluded_entities&&t.excluded_entities.includes(e)||c.includes(e.split(".",1)[0]))).sort()}(this.hass,e),show_header_toggle:!1});i.hass=this.hass,t.appendChild(i)}_hassChanged(e){const t=this.$.root;t.lastChild&&(t.lastChild.hass=e)}});var P=i(113);customElements.define("hui-view",class extends a.a{static get template(){return s["a"]`
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
    `}static get properties(){return{hass:{type:Object,observer:"_hassChanged"},config:Object,columns:Number}}static get observers(){return["_createBadges(config)","_createCards(config, columns)"]}constructor(){super(),this._cards=[],this._badges=[]}_createBadges(e){const t=this.$.badges;for(;t.lastChild;)t.removeChild(t.lastChild);if(!e||!e.badges||!Array.isArray(e.badges))return t.style.display="none",void(this._badges=[]);const i=[];for(const s of e.badges){if(!(s in this.hass.states))continue;const e=document.createElement("ha-state-label-badge");e.state=this.hass.states[s],i.push({element:e,entityId:s}),t.appendChild(e)}this._badges=i,t.style.display=i.length>0?"block":"none"}_createCards(e){const t=this.$.columns;for(;t.lastChild;)t.removeChild(t.lastChild);if(!e)return void(this._cards=[]);const i=e.cards.map(e=>{const t=B(e);return t.hass=this.hass,t});let s=[];const a=[];for(let e=0;e<this.columns;e++)s.push([]),a.push(0);i.forEach(e=>{this.appendChild(e);const t="function"==typeof e.getCardSize?e.getCardSize():1;s[function(e){let t=0;for(let e=0;e<a.length;e++){if(a[e]<5){t=e;break}a[e]<a[t]&&(t=e)}return a[t]+=e,t}(t)].push(e)}),(s=s.filter(e=>e.length>0)).forEach(e=>{const i=document.createElement("div");i.classList.add("column"),e.forEach(e=>i.appendChild(e)),t.appendChild(i)}),this._cards=i,"theme"in e&&Object(P.a)(t,this.hass.themes,e.theme)}_hassChanged(e){this._badges.forEach(t=>{const{element:i,entityId:s}=t;i.setProperties({hass:e,state:e.states[s]})}),this._cards.forEach(t=>{t.hass=e})}});const V={};customElements.define("hui-root",class extends(Object(r.a)(Object(n.a)(a.a))){static get template(){return s["a"]`
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
    `}static get properties(){return{narrow:Boolean,showMenu:Boolean,hass:{type:Object,observer:"_hassChanged"},config:{type:Object,observer:"_configChanged"},columns:{type:Number,observer:"_columnsChanged"},_curView:{type:Number,value:0},route:{type:Object,observer:"_routeChanged"},routeData:Object}}constructor(){super(),this._debouncedConfigChanged=z(()=>this._selectView(this._curView),100)}_routeChanged(e){const t=this.config&&this.config.views;if(""===e.path&&"/lovelace"===e.prefix&&t)this.navigate(`/lovelace/${t[0].id||0}`,!0);else if(this.routeData.view){const e=this.routeData.view;let i=0;for(let s=0;s<t.length;s++)if(t[s].id===e||s===parseInt(e)){i=s;break}i!==this._curView&&this._selectView(i)}}_computeViewId(e,t){return e||t}_computeTitle(e){return e.title||"Home Assistant"}_computeTabsHidden(e){return e.length<2}_computeTabTitle(e){return e||"Unnamed view"}_handleRefresh(){this.fire("config-refresh")}_handleUnusedEntities(){this._selectView("unused")}_deselect(e){e.target.selected=null}_handleHelp(){window.open("https://developers.home-assistant.io/docs/en/lovelace_index.html","_blank")}_handleViewSelected(e){const t=e.detail.selected;if(t!==this._curView){const e=this.config.views[t].id||t;this.navigate(`/lovelace/${e}`)}var i,s,a,n,r,o,c;i=this,s=this.$.layout.header.scrollTarget,a=s,n=Math.random(),r=Date.now(),o=a.scrollTop,c=0-o,i._currentAnimationId=n,function e(){var t,s=Date.now()-r;s>200?a.scrollTop=0:i._currentAnimationId===n&&(a.scrollTop=(t=s,-c*(t/=200)*(t-2)+o),requestAnimationFrame(e.bind(i)))}.call(i)}_selectView(e){this._curView=e;const t=this.$.view;let i;t.lastChild&&t.removeChild(t.lastChild);let s=this.config.background||"";if("unused"===e)(i=document.createElement("hui-unused-entities")).config=this.config;else{const e=this.config.views[this._curView];e.panel?(i=B(e.cards[0])).isPanel=!0:((i=document.createElement("hui-view")).config=e,i.columns=this.columns),e.background&&(s=e.background)}this.$.view.style.background=s,i.hass=this.hass,t.appendChild(i)}_hassChanged(e){this.$.view.lastChild&&(this.$.view.lastChild.hass=e)}_configChanged(e){this._loadResources(e.resources||[]),this._selectView(this._curView),this.$.view.classList.toggle("tabs-hidden",e.views.length<2)}_columnsChanged(e){this.$.view.lastChild&&(this.$.view.lastChild.columns=e)}_loadResources(e){e.forEach(e=>{switch(e.type){case"js":if(e.url in V)break;V[e.url]=Object(o.a)(e.url);break;case"module":Object(o.b)(e.url);break;case"html":Promise.resolve().then(i.bind(null,107)).then(({importHref:t})=>t(e.url));break;default:console.warn("Unknown resource type specified: ${resource.type}")}})}}),customElements.define("ha-panel-lovelace",class extends a.a{static get template(){return s["a"]`
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
    `}static get properties(){return{hass:Object,narrow:{type:Boolean,value:!1},showMenu:{type:Boolean,value:!1},route:Object,_columns:{type:Number,value:1},_state:{type:String,value:"loading"},_errorMsg:String,_config:{type:Object,value:null}}}static get observers(){return["_updateColumns(narrow, showMenu)"]}ready(){this._fetchConfig(),this._updateColumns=this._updateColumns.bind(this),this.mqls=[300,600,900,1200].map(e=>{const t=matchMedia(`(min-width: ${e}px)`);return t.addListener(this._updateColumns),t}),this._updateColumns(),super.ready()}_updateColumns(){const e=this.mqls.reduce((e,t)=>e+t.matches,0);this._columns=Math.max(1,e-(!this.narrow&&this.showMenu))}_fetchConfig(){this.hass.connection.sendMessagePromise({type:"frontend/lovelace_config"}).then(e=>this.setProperties({_config:e.result,_state:"loaded"}),e=>this.setProperties({_state:"error",_errorMsg:e.message}))}_equal(e,t){return e===t}})},76:function(e,t,i){"use strict";function s(e,t,i){return new Promise(function(s,a){const n=document.createElement(e);let r="src",o="body";switch(n.onload=(()=>s(t)),n.onerror=(()=>a(t)),e){case"script":n.async=!0,i&&(n.type=i);break;case"link":n.type="text/css",n.rel="stylesheet",r="href",o="head"}n[r]=t,document[o].appendChild(n)})}i.d(t,"a",function(){return a}),i.d(t,"b",function(){return n});const a=e=>s("script",e),n=e=>s("script",e,"module")}}]);
//# sourceMappingURL=140cb457d3247a098a70.chunk.js.map