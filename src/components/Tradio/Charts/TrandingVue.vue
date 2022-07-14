<template>
  <div id="tradingview_e8053">
    <VueTradingView
      :options="{
        width: '100%',
        height: 460,
        symbol: 'BITSTAMP:BTCUSD',
        interval: 'D',
        timezone: 'Etc/UTC',
        theme: dark ? 'dark' : 'Light',
        style: '1',
        locale: 'en',
        toolbar_bg: '#f1f3f6',
        enable_publishing: false,
        withdateranges: true,
        hide_side_toolbar: false,
        allow_symbol_change: true,
        show_popup_button: true,
        popup_width: '1000',
        popup_height: '650',
      }"
    />
  </div>
</template>

<script>
import VueTradingView from "vue-trading-view";

export default {
  name: "TrandingVue",
  components: {
    VueTradingView,
  },
  props: {
    dark: Boolean,
  },
};
</script>
