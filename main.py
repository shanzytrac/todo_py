import streamlit as st
#app title
st.title ("To Do List App")
#installation session state for task
if "tasks" not in st.session_state:
    st.session_state.task = {}
#sidebar hedding
st.sidebar.header("Manage Your Task")
#text input
new_task =st.sidebar.text_input("add a new task:",placeholder="Enter yuor task here....")
if st.Sidebar.button("Add Task"):
    if new_task.strip():
            st.session_state.tasks.append({"task" :new_task,"completed":False})
            st.success("task added successfuly")
    else:
              st. warning("Task can not be empty!")
#display task
st. subheader("your to do list")
if not st.session_state.tasks:
  st.info("no task added yet start by addiny a task form the sidebar!")
else:
    for index,task in enumerate("st.session_state.tasks"):
      coll,col2,col3=st.colums([0.7,0.15,0.15])
      # my tasks completed
      completed= col1.chekbox(f"**{task['tasks']}**",task["completed"],key=f"chek_{index}")
      if completed!=task["Completed"]: 
          st.session_state.task[index] ["completed"]=completed


           #update Task
      if col2.button("Edite",key=f"edite_{index}"):
 
           new_task=st.text_input("edite task",task["task"],key=f"edite_{index}")
           if new_task and st.button("save",key=f'save_{index}'):
              st.session_state.tasks[index]["task"]=new_task
              st.experimantal_rerun()
 #delete task
      if cal3.button("Delete",key=f'delete_{index}'):
       st.session_state.task[index]
      st.experimantal_rerun()
#clear all task
      if st.button("clear all task"):
       st.session_state.tasks=[] 
    st.success("All task deleted successfuly") 
 # Footer
    st.markdown("----")
    st.caption("sty organized and productive with this simpal To Do List App.")            
