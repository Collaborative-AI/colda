jest.setTimeout(10000);
import { check_interaction, handle_assistor_username_list, handle_input_column_string } from '../../../src/utils'
function test_utils(){
  test('test_utils',()=>{  

    let assistor_username_string = ''
    let id_column = ''
    let data_column = ''
    let target_column = ''
    let max_index = 0
    let handle_assistor_username_list_res = ''
    let check_interaction_res = ''

    handle_assistor_username_list_res = handle_assistor_username_list('xie2  , le1')  
    expect(handle_assistor_username_list_res).toEqual(['xie2', 'le1'])
    id_column = '1'
    data_column = '2-6'
    target_column = '7'
    max_index = 8
    id_column = handle_input_column_string(id_column, 'id', max_index)
    expect(id_column).toEqual('1')
    data_column = handle_input_column_string(data_column, 'data', max_index)
    expect(data_column).toEqual('2-6')
    target_column = handle_input_column_string(target_column, 'target', max_index)
    expect(target_column).toEqual('7')
    check_interaction_res = check_interaction(id_column, data_column, target_column)
    expect(check_interaction_res).toEqual(true)


    handle_assistor_username_list_res = handle_assistor_username_list('xie2  ,/le1')  
    expect(handle_assistor_username_list_res).toEqual(['xie2', '/le1'])
    id_column = '1  '
    data_column = '2  -  5'
    target_column = '  7'
    max_index = 8
    id_column = handle_input_column_string(id_column, 'id', max_index)
    expect(id_column).toEqual('1')
    data_column = handle_input_column_string(data_column, 'data', max_index)
    expect(data_column).toEqual('2-5')
    target_column = handle_input_column_string(target_column, 'target', max_index)
    expect(target_column).toEqual('7')
    check_interaction_res = check_interaction(id_column, data_column, target_column)
    expect(check_interaction_res).toEqual(true)

    handle_assistor_username_list_res = handle_assistor_username_list('xie2 le1')  
    expect(handle_assistor_username_list_res).toEqual(false)
    id_column = '1'
    data_column = '2-6'
    target_column = '7'
    max_index = 5
    id_column = handle_input_column_string(id_column, 'id', max_index)
    expect(id_column).toEqual('1')
    data_column = handle_input_column_string(data_column, 'data', max_index)
    expect(data_column).toEqual(false)
    target_column = handle_input_column_string(target_column, 'target', max_index)
    expect(target_column).toEqual(false)
    check_interaction_res = check_interaction(id_column, data_column, target_column)
    expect(check_interaction_res).toEqual(false)

    handle_assistor_username_list_res = handle_assistor_username_list('xie2  ,/ le1')  
    expect(handle_assistor_username_list_res).toEqual(false)
    id_column = '01'
    data_column = '2-06'
    target_column = ',7'
    max_index = 8
    id_column = handle_input_column_string(id_column, 'id', max_index)
    expect(id_column).toEqual(false)
    data_column = handle_input_column_string(data_column, 'data', max_index)
    expect(data_column).toEqual(false)
    target_column = handle_input_column_string(target_column, 'target', max_index)
    expect(target_column).toEqual(false)
    check_interaction_res = check_interaction(id_column, data_column, target_column)
    expect(check_interaction_res).toEqual(false)

    handle_assistor_username_list_res = handle_assistor_username_list(' xie2le1')  
    expect(handle_assistor_username_list_res).toEqual(['xie2le1'])
    id_column = '1,2'
    data_column = '6-2'
    target_column = ' 7+'
    max_index = 8
    id_column = handle_input_column_string(id_column, 'id', max_index)
    expect(id_column).toEqual(false)
    data_column = handle_input_column_string(data_column, 'data', max_index)
    expect(data_column).toEqual(false)
    target_column = handle_input_column_string(target_column, 'target', max_index)
    expect(target_column).toEqual(false)
    check_interaction_res = check_interaction(id_column, data_column, target_column)
    expect(check_interaction_res).toEqual(false)

    handle_assistor_username_list_res = handle_assistor_username_list('  xie2~l e1')  
    expect(handle_assistor_username_list_res).toEqual(false)
    id_column = '1,2'
    data_column = '62'
    target_column = ' 7 '
    max_index = 8
    id_column = handle_input_column_string(id_column, 'id', max_index)
    expect(id_column).toEqual(false)
    data_column = handle_input_column_string(data_column, 'data', max_index)
    expect(data_column).toEqual(false)
    target_column = handle_input_column_string(target_column, 'target', max_index)
    expect(target_column).toEqual('7')
    check_interaction_res = check_interaction(id_column, data_column, target_column)
    expect(check_interaction_res).toEqual(false)

  })
}

let test_utils_helper = {}
test_utils_helper.test_utils = test_utils

export { test_utils_helper}