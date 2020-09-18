import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import Register from "../components/Register";
import Index from "../components/Index";
import Addemp from "../components/Addemp";
import Update from "../components/Update";
Vue.use(Router);
const VueRouterPush = Router.prototype.push ;
Router.prototype.push = function push (to) {
    return VueRouterPush.call(this, to).catch(err => err)
};


export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login,
    },
    {
      path: '/login',
      name: 'login',
      component:Login,
    },
    {
      path: '/register',
      name: 'register',
      component:Register,
    },
      {
      path: '/index',
      name: 'insex',
      component:Index,
    },
      {
      path: '/addemp',
      name: 'addemp',
      component:Addemp,
    },
      {
      path: '/update',
      name: 'update',
      component:Update,
    },
       {
      // path: '/update/:id/:emp_name/:salary/:age',
      path: '/update/:id',
      name: 'update',
      component:Update,
    },
  ]
})
