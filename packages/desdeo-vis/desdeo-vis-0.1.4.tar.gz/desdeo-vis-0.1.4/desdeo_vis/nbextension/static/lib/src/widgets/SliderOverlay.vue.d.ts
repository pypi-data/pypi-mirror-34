import { Vue } from "vue-property-decorator";
import { SliderConf, DimPref } from './utils';
export default class SliderOverlay extends Vue {
    conf: SliderConf;
    pref: DimPref;
    readonly value: number;
    readonly step: string;
    readonly style: {
        left: string;
        top: string;
        width: string;
        transform: string;
    };
    valueChange(input: any): void;
    updatePref(pref: DimPref): void;
}
