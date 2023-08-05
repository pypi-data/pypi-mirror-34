import { Vue } from "vue-property-decorator";
import { DimPref, SliderConf } from './utils';
export default class PrefInput extends Vue {
    conf: SliderConf;
    pref: DimPref;
    readonly PREF_KINDS: string[];
    kindChange(input: any): void;
    valueChange(input: any): void;
    updatePref(pref: DimPref): void;
    readonly hasValue: boolean;
    readonly value: number | null;
    readonly dispKinds: string[];
}
