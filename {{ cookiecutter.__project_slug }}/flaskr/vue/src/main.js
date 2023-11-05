import './style.css'
import { createApp, h } from 'vue';
import { createInertiaApp } from '@inertiajs/vue3';

// create a plugin to use window.reverseUrl in our Components
const routePlugin = {
  install: (app, _options) => {
    app.config.globalProperties.$route = window.reverseUrl;
  }
}

createInertiaApp({
  resolve: async name => {
    const page = await import(`./pages/${name}.vue`);
    return page.default;
  },
  setup({ el, App, props, plugin }) {
    const vueApp = createApp({ render: () => h(App, props) });
    vueApp.use(plugin);
    vueApp.use(routePlugin);
    vueApp.mount(el);
  }
})
