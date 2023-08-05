import { Vue } from "vue-property-decorator";
import * as vega from 'vega';
import { SliderConf, DimPref } from './utils';
import SliderOverlay from './SliderOverlay.vue';
import NimbusPrefSettings from './NimbusPrefSettings.vue';
export default class NimbusPref extends Vue {
    $refs: {
        vega: Element;
        sliders: SliderOverlay[];
        settings: NimbusPrefSettings;
    };
    confs: SliderConf[];
    vegaView: vega.View;
    vegaEl: Element;
    maximized: boolean[];
    maxAsMin: boolean;
    initPreferences: DimPref[] | null;
    preferences: {
        pref: DimPref;
    }[];
    initialPreferences(): {
        pref: DimPref;
    }[];
    mounted(): void;
    readonly problem: string | null;
    readonly prefs: DimPref[];
    readonly curMaxAsMin: boolean;
}
