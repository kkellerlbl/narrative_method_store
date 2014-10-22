/*

*/
module NarrativeMethodStore {

    /* Returns the current running version of the NarrativeMethodStore. */
    funcdef ver() returns (string);

    /* @range [0,1] */
    typedef int boolean;
    
    typedef string url;
    typedef string username;
    typedef string email;

    typedef structure {
	string id;
	string name;
	string ver;
	string tooltip;
	string description;
	list<string> parent_ids;
	string loading_error;
    } Category;

    /* Minimal information about a method suitable for displaying the method in a menu or navigator. */
    typedef structure {
        string id;
        string name;
        string ver;
        string subtitle;
        string tooltip;
        list<string> categories;
        string loading_error;
    } MethodBriefInfo;
    
    typedef structure {
        url url;
    } ScreenShot;
    
    /* Full information about a method suitable for displaying a method landing page. */
    typedef structure {
        string id;
        string name;
        string ver;
        list <username> authors;
        email contact;
        
        string subtitle;
        string tooltip;
        string description;
        string technical_description;
        
        list<string> categories;
        
        list<ScreenShot> screenshots;
        
    } MethodFullInfo;

    /* specify the input / ouput widgets used for rendering */
    typedef structure {
        string input;
        string output;
    } WidgetSpec;




    /*
        valid_ws_types  - list of valid ws types that can be used for input
        validate_as     - int | float | nonnumeric | none
    */
    typedef structure {
        list <string> valid_ws_types;
        string validate_as;
    } TextOptions;

    typedef structure {
        int n_rows;
    } TextAreaOptions;
    
    typedef structure {
        int min;
        int max;
        int step;
    } IntSliderOptions;
    
    typedef structure {
        float min;
        float max;
    } FloatSliderOptions;
    
    
    typedef structure {
        int checked_value;
        int unchecked_value;
    } CheckboxOptions;
    
    typedef structure {
        mapping<string,string> ids_to_options;
    } DropdownOptions;
    
    typedef structure {
        mapping<string,string> ids_to_options;
        mapping<string,string> ids_to_tooltip;
    } RadioOptions;

    /*
        Description of a method parameter.
        @optional text_options textarea_options intslider_options checkbox_options
        @optional dropdown_options radio_options
    */
    typedef structure {
        string id;
        string ui_name;
        string short_hint;
        string long_hint;
        string field_type;
        boolean allow_multiple;
        boolean optional;
        boolean advanced;
        
        list<string> default_values;
        
        TextOptions text_options;
        TextAreaOptions textarea_options;
        IntSliderOptions intslider_options;
        FloatSliderOptions floatslider_options;
        CheckboxOptions checkbox_options;
        DropdownOptions dropdown_options;
        RadioOptions radio_options;
        
    } MethodParameter;
    
    /*
    	prefix - optional string concatenated before generated part
    	symbols - number of generated characters, optional, default is 8
    	suffix - optional string concatenated after generated part
    	@optional prefix symbols suffix
    */
    typedef structure {
        string prefix;
        int symbols;
        string suffix;
    } AutoGeneratedValue;
    
    /*
        input_parameter - parameter_id, if not specified then one of 'constant_value' or 
            'narrative_system_variable' should be set.
        constant_value - constant value, could be even map/array, if not specified then 'input_parameter' or
            'narrative_system_variable' should be set.
        narrative_system_variable - name of internal narrative framework property, currently only these names are
            supported: 'workspace', 'token', 'user_id'; if not specified then one of 'input_parameter' or
            'constant_value' should be set.
        generated_value - automatically generated value; it could be used as independent mode or when another mode 
            finished with empty value (for example in case 'input_parameter' is defined but value of this
            parameter is left empty by user); so this mode has lower priority when used with another mode.
        target_argument_position - position of argument in RPC-method call, optional field, default value is 0.
        target_property - name of field inside structure that will be send as arguement. Optional field,
            in case this field is not defined (or null) whole object will be sent as method argument instead of
            wrapping it by structure with inner property defined by 'target_property'.
        target_type_transform - none/string/int/float/ref, optional field, default is 'none' (it's in plans to
            support list<type>, mapping<type> and tuple<t1,t2,...> transformations).
        @optional input_parameter constant_value narrative_system_variable generated_value 
        @optional target_argument_position target_property target_type_transform
    */
    typedef structure {
        string input_parameter;
        UnspecifiedObject constant_value;
        string narrative_system_variable;
        AutoGeneratedValue generated_value;
        int target_argument_position;
        string target_property;
        string target_type_transform;
    } ServiceMethodInputMapping;

    /*
        input_parameter - parameter_id, if not specified then one of 'constant_value' or 
            'narrative_system_variable' should be set.
        service_method_output_path - list of properties and array element positions defining JSON-path traversing
            through which we can find necessary value. 
        constant_value - constant value, could be even map/array, if not specified then 'input_parameter' or
            'narrative_system_variable' should be set.
        narrative_system_variable - name of internal narrative framework property, currently only these names are
            supported: 'workspace', 'token', 'user_id'; if not specified then one of 'input_parameter' or
            'constant_value' should be set.
        target_property - name of field inside structure that will be send as arguement. Optional field,
            in case this field is not defined (or null) whole object will be sent as method argument instead of
            wrapping it by structure with inner property defined by 'target_property'.
        target_type_transform - none/string/int/float/list<type>/mapping<type>/ref, optional field, default is 
            no transformation.
        @optional input_parameter service_method_output_path constant_value narrative_system_variable 
        @optional target_property target_type_transform
    */
    typedef structure {
        string input_parameter;
        list<string> service_method_output_path;
        UnspecifiedObject constant_value;
        string narrative_system_variable;
        string target_property;
        string target_type_transform;
    } ServiceMethodOutputMapping;

    /*
        Determines how the method is handled when run.
        kb_service_name - name of service which will be part of fully qualified method name, optional field (in
            case it's not defined developer should enter fully qualified name with dot into 'kb_service_method'.
        kb_service_input_mapping - mapping from input parameters to input service method arguments.
        kb_service_output_mapping - mapping from output of service method to final output of narrative method.
        @optional python_function kb_service_name kb_service_method kb_service_input_mapping kb_service_output_mapping
    */
    typedef structure {
        string python_class;
        string python_function;
        string kb_service_url;
        string kb_service_name;
        string kb_service_method;
        list<ServiceMethodInputMapping> kb_service_input_mapping;
        list<ServiceMethodOutputMapping> kb_service_output_mapping;
    } MethodBehavior;

    /*
        The method specification which should provide enough information to render a default
        input widget for the method.
    */
    typedef structure {
        MethodBriefInfo info;
        
        WidgetSpec widgets;
        list<MethodParameter> parameters;
        
        MethodBehavior behavior;

        string job_id_output_field;
    } MethodSpec;



    
    typedef structure {
        string id;
        string name;
        string ver;
        string subtitle;
        string tooltip;
        list<string> categories;
        string loading_error;
    } AppBriefInfo;

    typedef structure {
        string id;
        string name;
        string ver;
        list <username> authors;
        email contact;
        
        string subtitle;
        string tooltip;
        
        string header;
        
        string description;
        string technical_description;
        
        list<string> categories;
        
        list<ScreenShot> screenshots;
    } AppFullInfo;
    
    /*
        Defines how any input to a particular step should be
        populated based 
        step_source - the id of the step to pull the parameter from
        isFromInput - set to true (1) to indicate that the input should be pulled from the input
            parameters of the step_source.  This is the only supported option.  In the future, it
            may be possible to pull the input from the output of the previous step (which would
            require special handling of the app runner).
        from - the id of the input parameter/output field in step_source to retrieve the value
        to - the name of the parameter to automatically populate in this step
        transformation - not supported yet, but may be used to indicate if a transformation of the
            value should occur when mapping the input to this step
        //@optional transformation
    */
    typedef structure {
        string step_source;
        boolean isFromInput;
        string from;
        string to;
    } AppStepInputMapping;
    
    typedef structure {
        string step_id;
        string method_id;
        list<AppStepInputMapping> input_mapping;
    } AppSteps;
    
    /* typedef structure {
    
    } AppBehavior; */
    
    typedef structure {
        AppBriefInfo info;
        
        list<AppSteps> steps;

    } AppSpec;




    /*
        List all the categories.  Optionally, if load_methods or load_apps are set to 1,
        information about all the methods and apps is provided.  This is important
        load_methods - optional field (default value is 1)
    */
    typedef structure {
        boolean load_methods;
        boolean load_apps;
    } ListCategoriesParams;

    funcdef list_categories(ListCategoriesParams params) 
                returns ( mapping<string, Category> categories,
                          mapping<string, MethodBriefInfo> methods,
                          mapping<string, AppBriefInfo> apps);

    typedef structure {
        list <string> ids;
    } GetCategoryParams;

    funcdef get_category(GetCategoryParams params) returns (list<Category>);

    /*
        These parameters do nothing currently, but are a placeholder for future options
        on listing methods or apps
        limit - optional field (default value is 0)
        offset - optional field (default value is 0)
    */
    typedef structure {
        int limit;
        int offset;
    } ListParams;
    
    funcdef list_methods(ListParams params) returns (list<MethodBriefInfo>);
    
    funcdef list_methods_full_info(ListParams params) returns (list<MethodFullInfo>);
    
    funcdef list_methods_spec(ListParams params) returns (list<MethodSpec>);

    funcdef list_method_ids_and_names() returns (mapping<string,string>);
    
    
    funcdef list_apps(ListParams params) returns (list<AppBriefInfo>);
    
    funcdef list_apps_full_info(ListParams params) returns (list<AppFullInfo>);
    
    funcdef list_apps_spec(ListParams params) returns (list<AppSpec>);
    
    funcdef list_app_ids_and_names() returns (mapping<string,string>);
    
    
    typedef structure {
        list <string> ids;
    } GetMethodParams;

    funcdef get_method_brief_info(GetMethodParams params) returns (list<MethodBriefInfo>);
    
    funcdef get_method_full_info(GetMethodParams params) returns (list<MethodFullInfo>);
    
    funcdef get_method_spec(GetMethodParams params) returns (list<MethodSpec>);
    
    
    
    typedef structure {
        list <string> ids;
    } GetAppParams;

    funcdef get_app_brief_info(GetAppParams params) returns (list<AppBriefInfo>);
    
    funcdef get_app_full_info(GetAppParams params) returns (list<AppFullInfo>);
    
    funcdef get_app_spec(GetAppParams params) returns (list<AppSpec>);
    

};