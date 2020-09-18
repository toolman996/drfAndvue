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
						update Emp info:{{$route.params.id}}
					</h1>
					<form action="emplist.html" method="post">
						<table cellpadding="0" cellspacing="0" border="0"
							class="form_table">
							<tr>
								<td valign="middle" align="right">
									id:
								</td>
								<td valign="middle" align="left">
									{{emp_id}}
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									name:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="name" v-model="emp_name"/>
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									photo:
								</td>
								<td valign="middle" align="left">
                                    <img :src="emp_img" alt="" width="60" height="60"><br>
                                    <input type="file" name="photo" ref="img"/>

<!--									<input type="file" name="photo"/>-->
<!--                                    <img :src="emp_img" alt="">-->
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									salary:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="salary" v-model="emp_salary"/>
								</td>
							</tr>
							<tr>
								<td valign="middle" align="right">
									age:
								</td>
								<td valign="middle" align="left">
									<input type="text" class="inputgri" name="age" v-model="emp_age"/>
								</td>
							</tr>
						</table>
						<p>
							<input type="button" class="button" value="Confirm" @click="click" />
						</p>
					</form>
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
        name: "Update",
        data(){
            return{
                emp_id:'',
                emp_name:'',
                emp_salary:'',
                emp_age:'',
                emp_img:'',
            }
        },
        methods:{

            lly(){

                let emp_id=this.$route.params.id
                this.$axios.get('http://127.0.0.1:8000/emsapp/emp/'+`${emp_id}`).then(res=>{
                            this.emp_id=res.data.result['id']
                            this.emp_name=res.data.result['emp_name']
                            this.emp_salary=res.data.result['salary']
                            this.emp_age=res.data.result['age']
                            this.emp_img=res.data.result['img']

                }).catch(error=>{
                    this.$message('没有信息');
                })
            },
            click() {
                    let formData = new FormData();
                    formData.append("emp_name", this.emp_name);
                    formData.append("img", this.$refs.img.files[0]);
                    formData.append("salary", this.emp_salary);
                    formData.append("age", this.emp_age);
                    this.$axios({
                        url: "http://127.0.0.1:8000/emsapp/emp/"+`${this.emp_id}`,
                        method: "patch",
                        data: formData,
                        headers:{
                            'content-type': 'multipart/form-data',
                        },
                    }).then(res => {
                        console.log(res.data.result)
                        this.$message('修改成功');
                        this.$router.push('/index')
                    }).catch(error => {
                        this.$message.error("修改失败")
                    })
            }

        },
        created() {
            this.lly()
        }
    }
</script>

<style scoped>

</style>
