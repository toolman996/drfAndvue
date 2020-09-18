<template>
    <div id="wrap">
			<div id="top_content">
					<div id="header">
						<div id="rightheader">
							<p>
								2009/11/20
								<br />
							</p>
						</div>
						<div id="topheader">
							<h1 id="title">
								<a href="#">Main</a>
							</h1>
						</div>
						<div id="navigation">
						</div>
					</div>
				<div id="content">
					<p id="whereami">
					</p>
					<h1>
						add Emp info:
					</h1>
						<table cellpadding="0" cellspacing="0" border="0"
							class="form_table">
							<tr>
								<td valign="middle" align="right">
									name:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="name" v-model="emp_name" />
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									photo:
								</td>
								<td valign="middle" align="left">
									<input type="file" name="photo" ref="img"/>
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									salary:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="salary" v-model="salary" />
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									age:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="age" v-model="age" />
								</td>
							</tr>
						</table>
						<p>
							<input type="submit" class="button" value="添加员工" @click="add" />
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
        name: "Addemp",
        data(){
            return{
                emp_name:'',
                img:'',
                salary:'',
                age:''
            }
        },
        methods:{
            add(){
                let formData = new FormData();
                formData.append("emp_name", this.emp_name);
                formData.append("img", this.$refs.img.files[0]);
                formData.append("salary", this.salary);
                formData.append("age", this.age);
                this.$axios({
                url:'http://127.0.0.1:8000/emsapp/emp/',
                method:'post',
                data:formData,
                headers:{
                    'content-type': 'multipart/form-data'
                },
              }).then(res=>{
                  // console.log(res.data);
                  // if(res.data['message']){
                  //     //注册成功自动跳转到登录页面
                  //     // this.$message('恭喜你注册成功');
                  //     let kk=res.data.result['username']
                  //     // sessionStorage.setItem('name',JSON.stringify(username))
                  //     sessionStorage.setItem('user',kk)
                      this.$router.push('/index')
                  // }

              }).catch(error=>{
                  this.$message.error('用户不存在');
              })
            }
        },
        created() {
            let bt=sessionStorage.getItem('user')

            if (bt){

            }else {
                this.$message.error('请先登录')
                this.$router.push('/login')
            }

        }
    }
</script>

<style scoped>

</style>
