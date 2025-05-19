from selenium.webdriver.common.by import By


# 封装产品详情的页面元素定位
class ProductPage:
    """========================定制按钮的元素==========================="""
    customizer_button_buy = By.CSS_SELECTOR, 'button.sunzi__button-custom-BHul3'
    customizer_button_buy1 = By.CSS_SELECTOR, 'button.sunzi__button-custom-XJJa8'
    customizer_button_buy2 = By.CSS_SELECTOR, 'button#sunzi-button'
    customizer_button_buy3 = By.CSS_SELECTOR, 'div.sunzi__button-s-s1R'
    customizer_button_buy4 = By.CSS_SELECTOR, 'button.sunzi__button-custom-ovWhK'
    customizer_button_buy6 = By.CSS_SELECTOR, 'div.sunzi-photo-wallet-lite>button'
    customizer_button_buy8 = By.CSS_SELECTOR, 'div.sunzi-film-strip>button'
    customizer_button_buy9 = By.CSS_SELECTOR, 'button#sunzi-button>input'
    customizer_button_buy10 = By.CSS_SELECTOR, 'div.tw-relative>div'
    customizer_button_buy11 = By.CSS_SELECTOR, 'button#AddToCart-product-dog'
    customizer_button_buy12 = By.CSS_SELECTOR, 'button.sunzi__button-custom-WtKpn'
    customizer_button_buy13 = By.CSS_SELECTOR, 'button.sunzi__button-custom-MmmX8'
    customizer_button_buy14 = By.CSS_SELECTOR, 'button.sunzi__button-custom-Ue-2M'
    customizer_button_buy15 = By.CSS_SELECTOR, 'button.sunzi__button-custom-aAwQ6'
    customizer_button_buy16 = By.CSS_SELECTOR, 'div.__button'

    """========================传图按钮的元素==========================="""
    img_input = By.CSS_SELECTOR, 'div.sunzi__content-3gwyl>div:nth-child(2)>input'
    img_input1 = By.CSS_SELECTOR, 'div.index-module_channel__3InO6.index-module_channelAlbum__2cfnH>input'
    img_input2 = By.CSS_SELECTOR, 'div.sunzi__text-box-203xG'
    img_input3 = By.CSS_SELECTOR, 'div.sunzi__next-2_dzF>input'
    img_input4 = By.CSS_SELECTOR, 'div.tw-relative>input'
    img_input5 = By.CSS_SELECTOR, 'div.sunzi__desktop-NRRPg>input'
    img_input6 = By.CSS_SELECTOR, 'div.sunzi_components__desktop-NRRPg>input'
    img_input7 = By.CSS_SELECTOR, 'div.sunzi__desktop-DGYFZ>input'
    img_input8 = By.CSS_SELECTOR, 'div.sunzi__content-group-local-MHKLM>input'
    img_input9 = By.CSS_SELECTOR, 'div.el-upload>input'
    img_input10 = By.CSS_SELECTOR, 'div.sunzi__bottom-content-camera-3A1mV>input'
    img_input11 = By.CSS_SELECTOR, 'input#sunzi-button-input'
    img_input12 = By.CSS_SELECTOR, 'div.upload-images>input'
    add_photo = By.CSS_SELECTOR, 'div.sunzi__button-I2owl'
    add_photo2 = By.CSS_SELECTOR, 'div.sunzi__text-box-10t3t>span'
    add_photo3 = By.CSS_SELECTOR, 'div.sunzi__button-3MuRS'
    add_photo4 = By.CSS_SELECTOR, 'div.sunzi__item-info-rL69R'

    """========================选择图层的元素==========================="""
    person_photo = By.CSS_SELECTOR, 'div.sunzi__box-mhyfd'
    person_photo1 = By.CSS_SELECTOR, 'div.sunzi__button-hEI30'
    person_photo2 = By.CSS_SELECTOR, 'div.sunzi__icon-wrapper-hVMnb'
    person_photo3 = By.CSS_SELECTOR, 'div.sunzi__box-KN3ZB'
    view_photo = By.CSS_SELECTOR, 'div.sunzi__face-img-wIuDY'

    """========================加车成功文案弹窗的元素==========================="""
    addcart_success_text = By.CSS_SELECTOR, 'div.tt'
    addcart_success_text2 = By.CSS_SELECTOR, 'div.trade-cart-banner-title'
    addcart_success_text3 = By.CSS_SELECTOR, 'div.tingle-modal-box__content>div>ul>li'
    addcart_success_text4 = By.CSS_SELECTOR, 'div.msg-box>p'
    addcart_success_text5 = By.CSS_SELECTOR, 'div.mm-cart-popup__button>p'
    addcart_success_text6 = By.CSS_SELECTOR, 'div.modal-tips>h1'

    """========================加车按钮的元素==========================="""
    addcart_button2 = By.CSS_SELECTOR, 'div.sunzi__button-2FTPg'
    addcart_button3 = By.CSS_SELECTOR, 'div.sunzi__preview-wrapper-2dB8l>div:nth-child(6)'
    addcart_button4 = By.CSS_SELECTOR, 'div.sunzi__button-DzDsD'
    addcart_button5 = By.CSS_SELECTOR, 'div.sunzi__confirm-3TjxC'
    addcart_button6 = By.CSS_SELECTOR, 'div.sunzi__custom-button-content-vGv0J'
    addcart_button8 = By.CSS_SELECTOR, 'div.sunzi__button-UKQGD'
    addcart_button9 = By.CSS_SELECTOR, 'div.sunzi__confirm-button-NG61P'
    addcart_button11 = By.CSS_SELECTOR, 'div.sunzi__confirm-button-3YQpi'
    addcart_button12 = By.CSS_SELECTOR, 'div.sunzi__denied-2B4du'
    addcart_button13 = By.CSS_SELECTOR, 'button.custom-mall-button'

    """========================下一步按钮的元素==========================="""
    next_button = By.CSS_SELECTOR, 'div.sunzi__text-botton-QiKpF'
    next_button1 = By.CSS_SELECTOR, 'div.sunzi__decorate-select-d5hTM>div>div:nth-child(2)'
    next_button3 = By.CSS_SELECTOR, 'div.sunzi__button-UKQGD'
    next_button4 = By.CSS_SELECTOR, 'div.sunzi-header-submit'
    next_button5 = By.CSS_SELECTOR, 'div.sunzi__confirm-zbYBX'
    next_button7 = By.CSS_SELECTOR, 'div.sunzi__float-8hNkN>div'
    next_button8 = By.CSS_SELECTOR, 'div.sunzi__header-submit-3G1lZ'
    next_button9 = By.CSS_SELECTOR, 'div.sunzi__button-MpY5R'
    next_button10 = By.CSS_SELECTOR, 'div.sunzi__custom-yKExo>div>div:nth-child(3)'
    next_button11 = By.CSS_SELECTOR, 'div.index-module_confirmButton__3G-xH'
    next_button12 = By.CSS_SELECTOR, 'div.sunzi__confirm-button-jLTJO'
    next_button13 = By.CSS_SELECTOR, 'div.sunzi__header-submit-icon-2DAao'
    next_button14 = By.CSS_SELECTOR, 'div.sunzi__panel--confirm-vlyhm'
    next_button15 = By.CSS_SELECTOR, 'div.tw-align-center'
    next_button16 = By.CSS_SELECTOR, 'button.el-button'
    next_button17 = By.CSS_SELECTOR, 'div.sunzi__button-2Oeyo'
    next_button18 = By.CSS_SELECTOR, 'div.sunzi__button-MnxT2'
    next_button19 = By.CSS_SELECTOR, 'div.sunzi__header-confirm-198D_'
    next_button20 = By.CSS_SELECTOR, 'div.sunzi__button-W51rS'
    next_button21 = By.CSS_SELECTOR, 'div.sunzi__code-type-Re4Zp'
    next_button22 = By.CSS_SELECTOR, 'div.sunzi__input-confirm-iTbQa'
    next_button23 = By.CSS_SELECTOR, 'div.sunzi__button-confirm-c07p5'
    confirm_button2 = By.CSS_SELECTOR, 'div.sunzi__button-gKlPv'
    confirm_button3 = By.CSS_SELECTOR, 'div.sunzi__button-xkXmZ'
    confirm_button4 = By.CSS_SELECTOR, 'div.sunzi__next-2_dzF'
    confirm_button8 = By.CSS_SELECTOR, 'div.image-module_confirm__1plgV'
    confirm_button9 = By.CSS_SELECTOR, 'div.sunzi__button-D8ojT'
    confirm_button10 = By.CSS_SELECTOR, 'div.sunzi__preview-header-submit-eIMrt'
    confirm_button11 = By.CSS_SELECTOR, 'button.tingle-btn--primary'
    confirm_button12 = By.CSS_SELECTOR, 'div.tw-relative>svg'

    """===============选择刻字的元素==============="""
    custom_text_button = By.CSS_SELECTOR, 'div.sunzi__button-bZWRQ'

    """===============选择素材的元素==============="""
    material_radio = By.CSS_SELECTOR, 'div:nth-child(1).sunzi__img-box-PbrHf>img'
    material_radio5 = By.CSS_SELECTOR, 'div.sunzi__variant-option-item-vKPOI'
    material_radio6 = By.CSS_SELECTOR, 'div.sunzi__image-TLimO'
    material_radio7 = By.CSS_SELECTOR, 'div.sunzi__box-2yFOK'
    material_radio10 = By.CSS_SELECTOR, 'div.sunzi__img-box-2Ga24'

    """========================刻字定位的元素==========================="""
    text_input = By.CSS_SELECTOR, 'div.sunzi__input-box-cJHVL>input'
    text_input2 = By.CSS_SELECTOR, 'div.tw-relative>textarea'
    text_input3 = By.CSS_SELECTOR, 'div.text-input-container>input'
    text_input4 = By.CSS_SELECTOR, 'div.sunzi__item-content-Dq2nY>textarea'
    text_input5 = By.CSS_SELECTOR, 'div.sunzi__item-content-Dq2nY>input'
    text_input6 = By.CSS_SELECTOR, 'div.sunzi__input-box-UDBZR>input'
    text_input7 = By.CSS_SELECTOR, 'div.sunzi__type-content-ZBQks>textarea'
    text_input8 = By.CSS_SELECTOR, 'div.sunzi__input-content-UmHa7>input'
    text_input9 = By.CSS_SELECTOR, 'div.sunzi__input-content-dyFJp>input'
    text_input10 = By.CSS_SELECTOR, 'div.inner-border>input'
    text_input11 = By.CSS_SELECTOR, 'div.sunzi__text-PwiQ5>input'
    text_input12 = By.CSS_SELECTOR, 'div.sunzi__input-box-3C3ty>input'
    text_input13 = By.CSS_SELECTOR, 'div.inner-border>textarea'

    """========================加购产品的元素==========================="""
    additem_button = By.CSS_SELECTOR, 'div.sunzi__content-btns-btn-1qnk3'
    additem_button2 = By.CSS_SELECTOR, 'div.sunzi__key-buckle-button-yi0aO'
    additem_button3 = By.CSS_SELECTOR, 'div.sunzi__confirm-1ivsR'
    additem_button4 = By.CSS_SELECTOR, 'div.sunzi__add-cart-button-1QXcX'
    additem_button5 = By.CSS_SELECTOR, 'div.sunzi__footer-3GSgu>div'
    additem_button6 = By.CSS_SELECTOR, 'div.sunzi__thank-next-8zTGJ'
    additem_button7 = By.CSS_SELECTOR, 'div.sunzi__design-button-1J4mx'
    additem_button8 = By.CSS_SELECTOR, 'div.sunzi__cart-button-3kWMv'
    additem_button9 = By.CSS_SELECTOR, 'div.sunzi__button-2yTJi'
    additem_button10 = By.CSS_SELECTOR, 'div.sunzi__button-1Xfr8'
    additem_button11 = By.CSS_SELECTOR, 'div.sunzi__button-group--content-ouZSa>div'
    additem_button12 = By.CSS_SELECTOR, 'div.sunzi__custom-button-1SWBd'
    additem_button13 = By.CSS_SELECTOR, 'div.sunzi__track-xhyEu'
    additem_button14 = By.CSS_SELECTOR, 'div.sunzi__button-1x6hd'
    additem_button15 = By.CSS_SELECTOR, 'div.sunzi__button-2cxkS'
    additem_button16 = By.CSS_SELECTOR, 'div.sunzi__footer-1xhHx'
    additem_button17 = By.CSS_SELECTOR, 'div.sunzi__button-3SN7j'
    additem_button18 = By.CSS_SELECTOR, 'div.sunzi__button-1LUc0'
    additem_button19 = By.CSS_SELECTOR, 'div.sunzi__button-2sbJE'
    additem_button20 = By.CSS_SELECTOR, 'div.sunzi__button-SsSAV'
    additem_button21 = By.CSS_SELECTOR, 'div.sunzi__button-1DwmO'
    additem_button22 = By.CSS_SELECTOR, 'button.sunzi__button-35k3P'
    additem_button23 = By.CSS_SELECTOR, 'div.sunzi__button-box-rRTyl'
    additem_button24 = By.CSS_SELECTOR, 'div.sunzi__add-cart-iRXZ7'
    additem_button25 = By.CSS_SELECTOR, 'div.sunzi__button-1-p_z'

    """========================是否需要文案按钮的元素==========================="""
    notext_button = By.CSS_SELECTOR, 'div.sunzi__drawer-box-3XGZG>div:nth-child(6)'
    notext_button2 = By.CSS_SELECTOR, 'div.sunzi__not-text-cZn9z'
    notext_button3 = By.CSS_SELECTOR, 'div.sunzi__cancle-Me02q'
    notext_button4 = By.CSS_SELECTOR, 'div.sunzi__withou-text-pl3ai'
    notext_button5 = By.CSS_SELECTOR, 'div.sunzi__button-Rukde'

    """========================选择模版的元素==========================="""
    choose_template = By.CSS_SELECTOR, 'div.sunzi__image-load-31bVK'
    choose_template2 = By.CSS_SELECTOR, 'div.sunzi__image-4iaHG'
    choose_template3 = By.CSS_SELECTOR, 'div.sunzi__image-wrapper-1o0zO'
    choose_template4 = By.CSS_SELECTOR, 'div.sunzi__image-kNKcK'
    choose_template5 = By.CSS_SELECTOR, 'div.sunzi__image-wrapper-PIu5A'

    """========================选择变体的元素==========================="""
    choose_variant = By.CSS_SELECTOR, 'div.asdqweqwewq>div:nth-child(3)>div>select>option'
    choose_variant1 = By.CSS_SELECTOR, 'div.sunzi__choose-option-tip-1g_TB'

    """========================勾选VIP时间的元素==========================="""
    vip_radio = By.CSS_SELECTOR, 'div.sunzi__select-box-mywrd>div'
    vip_radio2 = By.CSS_SELECTOR, 'div.sunzi__select-box-10T-j'
    vip_radio3 = By.CSS_SELECTOR, 'div.add-cart-button'
    vip_radio4 = By.CSS_SELECTOR, 'div.sunzi__title-text-2B96p'
    vip_radio5 = By.CSS_SELECTOR, 'div.sunzi__select-icon-e0SsC'

    """========================音乐选项的元素==========================="""
    music_option = By.CSS_SELECTOR, 'div.sunzi__track-20JeN'
    music_option2 = By.CSS_SELECTOR, 'div.sunzi__track-D2s79'

    """=======================选择传图数量的元素========================"""
    num_photo = By.CSS_SELECTOR, 'div.sunzi__item-thumb-name-yV9dT'

    """========================返回选项的元素=========================="""
    back_button = By.CSS_SELECTOR, 'div.sunzi__header-pJxAB>div>div'

    """=======================处理图片失败的元素======================="""
    error_ele = By.CSS_SELECTOR, 'div.sunzi__api-mQ8tw'

    """=======================语种弹窗的元素======================="""
    pop_ups = By.CSS_SELECTOR, 'button.recommendation-modal__close-button'

    skip_button = By.CSS_SELECTOR, 'div.sunzi__button-Ttg2q'

    color_button = By.CSS_SELECTOR, 'div.tw-border'