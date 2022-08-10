export default {
  projectState: state => state.projectList,
  taskState: state => state.taskList,
  categoryState: state => state.categoryList,
  selectedProjectState: state => state.selectedProject,
  selectedCategoryState: state => state.selectedCategory
}
