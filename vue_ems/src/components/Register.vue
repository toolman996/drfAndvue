<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    注册
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            用户名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="username" v-model="username">
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            真实姓名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="real_name">
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="password">
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            确认密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="pwds">
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            性别:
                        </td>
                        <td valign="middle" align="left">
                            男
                            <input type="radio" class="inputgri" name="sex" value="m" checked="checked"
                                   @click="gender=0">
                            女
                            <input type="radio" class="inputgri" name="sex" value="f" @click="gender=1">
                        </td>
                    </tr>

                </table>
                <p>
                    <el-button plain @click="submit">注册</el-button>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                username: '',
                password: '',
                pwds: '',
                real_name: '',
                gender: 0,
            }
        },
        methods: {
            // but:function(event){
            //     if (this.password!==this.pwds){
            //         this.$message.error('请再次确认密码');
            //         this.password='',
            //         this.pwds='',
            //             return T
            //     }else if (this.password===this.pwds){
            //
            //     }
            // },
            //点击注册按钮向服务器发起注册请求
            submit() {
                if (this.password !== this.pwds) {
                    this.$message.error('请再次确认密码');
                    this.password = '',
                        this.pwds = ''
                    return;
                } else if (this.password === this.pwds) {
                    this.$axios({
                        url: 'http://127.0.0.1:8000/emsapp/post/',
                        method: 'post',
                        data: {
                            username: this.username,
                            password: this.password,
                            again_pwd:this.pwds,
                            real_name: this.real_name,
                            gender: this.gender,

                        }
                    }).then(res => {
                        // console.log(res.data);
                        if (res.data['message']) {
                            //注册成功自动跳转到登录页面
                            this.$message('恭喜你注册成功');
                            this.$router.push('/login')
                        }
                    }).catch(error => {
                        this.$message.error('您输入的信息错误，请重新输入');
                    })

                }

            }
        }
    }
</script>

<style scoped>

</style>
