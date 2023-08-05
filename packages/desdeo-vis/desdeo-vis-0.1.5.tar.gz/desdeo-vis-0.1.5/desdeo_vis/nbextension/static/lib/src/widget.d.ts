import { DOMWidgetModel, DOMWidgetView, ISerializers } from '@jupyter-widgets/base';
export declare class VegaModel extends DOMWidgetModel {
    defaults(): any;
    static serializers: ISerializers;
    static model_name: string;
    static model_module: string;
    static model_module_version: string;
    static view_name: string;
    static view_module: string;
    static view_module_version: string;
}
export declare class VegaView extends DOMWidgetView {
    spec: any;
    view: any;
    render(): void;
}
