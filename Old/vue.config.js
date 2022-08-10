const webpack = require('webpack')
module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? process.env.VUE_APP_BASE_URL
    : '/',

  configureWebpack: {
    plugins: [
      new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
      new webpack.ProvidePlugin({
        mapboxgl: 'mapbox-gl'
      })
    ],
    resolve: {
      alias: {
        vue$: 'vue/dist/vue.common.js',
        'jquery': 'jquery/src/jquery.js'
      }
    }
  }
}
