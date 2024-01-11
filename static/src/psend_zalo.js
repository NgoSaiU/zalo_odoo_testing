// /** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { useService } from "@web/core/utils/hooks";

// patch(ReceiptScreen, {
    // components: { ...ReceiptScreen.components },
// });

patch(ReceiptScreen.prototype, {

    setup() {
        super.setup();
        this.rpc = useService("rpc")
        this.orderUiState.inputPhoneNumber = ''
    },

    async onSendZalo() {
        console.log(this.orderUiState.inputPhoneNumber)
        console.log("ble bla...")
        const soDienThoai = this.orderUiState.inputPhoneNumber;
        const dinhDangSDT = '+84' + soDienThoai.slice(1);
        console.log('So dien thoai sau khi dinh dang: ' + dinhDangSDT);

        
        
        
        const actoken =  await this.orm.call("res.config.settings", "get_access_token")
        
        console.log("asess toketn: ", actoken);
        
        
            
        // const a = await this.rpc(`/pos/rpc/sendtemplate`,{phone:dinhDangSDT, accessToken: actoken});
        
        // console.log(a);

        const ob = this.currentOrder;
        console.log(ob);
        // const taxes = ob.orderlines.product.Target.taxes_id
        console.log("Thuế là: ")
        const taxId = this.currentOrder.orderlines[0].product.taxes_id[0];
        const taxes = this.currentOrder.orderlines[0].pos.taxes_by_id[taxId].amount;
        console.log(taxes);
        console.log("====");
        const total = this.orderAmountPlusTip ;
        console.log("Total = " + total);
        const name = ob.get_name();
        console.log("Name: " + name);
        console.log("====");


        // xuất ra được thông tin số điện thoại của người dùng.

        return
    },



});

