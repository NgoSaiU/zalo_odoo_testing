/* @odoo-module */

import { Composer } from "@mail/core/common/composer";
import { Typing } from "@mail/discuss/typing/common/typing";

import { patch } from "@web/core/utils/patch";

patch(Composer, {
    components: { ...Composer.components, Typing },
});

patch(Composer.prototype, {
    /**
     * @override
     */
    setup() {
        super.setup();
    },
   
    /**
     * @override
     */
    
    async sendMessage() {
        // Hàm gửi thông tin 
        // await super.sendMessage();
        // // this.stopTyping();
        // console.log('sendMessage');
        await this.processMessage(async (value) => {
            const postData = {
                attachments: this.props.composer.attachments,
                isNote: this.props.type === "note",
                mentionedChannels: this.props.composer.mentionedChannels,
                mentionedPartners: this.props.composer.mentionedPartners,
                cannedResponseIds: this.props.composer.cannedResponses.map((c) => c.id),
                parentId: this.props.messageToReplyTo?.message?.id,
            };
            console.log(postData);
            console.log("Value");
            console.log(value);
            await this._sendMessage(value, postData);

        });
        
    },
    
});

