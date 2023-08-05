import { Vue } from "vue-property-decorator";
import { SliderConf } from './utils';
import SliderOverlay from './SliderOverlay.vue';
export default class SliderBank extends Vue {
    $refs: {
        sliders: SliderOverlay[];
    };
    confs: SliderConf[];
    created(): void;
    readonly values: number[];
}
