/// <reference types="backbone" />
import * as widgets from '@jupyter-widgets/base';
import * as services from '@jupyterlab/services';
import * as Backbone from 'backbone';
export declare class MockComm {
    target_name: string;
    constructor();
    on_close(fn: Function | null): void;
    on_msg(fn: Function | null): void;
    _process_msg(msg: services.KernelMessage.ICommMsg): any;
    close(): string;
    send(): string;
    open(): string;
    comm_id: string;
    _on_msg: Function | null;
    _on_close: Function | null;
}
export declare class DummyManager extends widgets.ManagerBase<HTMLElement> {
    constructor();
    display_view(msg: services.KernelMessage.IMessage, view: Backbone.View<Backbone.Model>, options: any): Promise<any>;
    protected loadClass(className: string, moduleName: string, moduleVersion: string): Promise<any>;
    _get_comm_info(): Promise<{}>;
    _create_comm(): Promise<MockComm>;
    el: HTMLElement;
    testClasses: {
        [key: string]: any;
    };
}
export interface Constructor<T> {
    new (attributes?: any, options?: any): T;
}
export declare function createTestModel<T extends widgets.WidgetModel>(constructor: Constructor<T>, attributes?: any): T;
