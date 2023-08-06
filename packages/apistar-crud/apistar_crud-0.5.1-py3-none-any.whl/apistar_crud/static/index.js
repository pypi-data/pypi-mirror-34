(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["index"],{

/***/ "./admin/App.js":
/*!**********************!*\
  !*** ./admin/App.js ***!
  \**********************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _getPrototypeOf = __webpack_require__(/*! babel-runtime/core-js/object/get-prototype-of */ "./node_modules/babel-runtime/core-js/object/get-prototype-of.js");

var _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _possibleConstructorReturn2 = __webpack_require__(/*! babel-runtime/helpers/possibleConstructorReturn */ "./node_modules/babel-runtime/helpers/possibleConstructorReturn.js");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = __webpack_require__(/*! babel-runtime/helpers/inherits */ "./node_modules/babel-runtime/helpers/inherits.js");

var _inherits3 = _interopRequireDefault(_inherits2);

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _propTypes = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");

var _propTypes2 = _interopRequireDefault(_propTypes);

var _routes = __webpack_require__(/*! ./routes */ "./admin/routes/index.js");

var _routes2 = _interopRequireDefault(_routes);

__webpack_require__(/*! ./App.css */ "./admin/App.css");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var propTypes = {
  fetchMetadata: _propTypes2.default.func.isRequired
};

var App = function (_Component) {
  (0, _inherits3.default)(App, _Component);

  function App() {
    (0, _classCallCheck3.default)(this, App);
    return (0, _possibleConstructorReturn3.default)(this, (App.__proto__ || (0, _getPrototypeOf2.default)(App)).apply(this, arguments));
  }

  (0, _createClass3.default)(App, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      this.props.fetchMetadata();
    }
  }, {
    key: 'render',
    value: function render() {
      return _react2.default.createElement(
        'div',
        { className: 'App' },
        _react2.default.createElement(_routes2.default, null)
      );
    }
  }]);
  return App;
}(_react.Component);

App.propTypes = propTypes;

exports.default = App;

/***/ }),

/***/ "./admin/AppContainer.js":
/*!*******************************!*\
  !*** ./admin/AppContainer.js ***!
  \*******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _reactRedux = __webpack_require__(/*! react-redux */ "./node_modules/react-redux/es/index.js");

var _App = __webpack_require__(/*! ./App */ "./admin/App.js");

var _App2 = _interopRequireDefault(_App);

var _metadata = __webpack_require__(/*! ./ducks/metadata */ "./admin/ducks/metadata.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var mapStatetoProps = function mapStatetoProps(state) {
  return {};
};

var mapDispatchToProps = {
  fetchMetadata: _metadata.fetchMetadataRequest
};

exports.default = (0, _reactRedux.connect)(mapStatetoProps, mapDispatchToProps)(_App2.default);

/***/ }),

/***/ "./admin/api.js":
/*!**********************!*\
  !*** ./admin/api.js ***!
  \**********************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.REL_PATH = undefined;

var _stringify = __webpack_require__(/*! babel-runtime/core-js/json/stringify */ "./node_modules/babel-runtime/core-js/json/stringify.js");

var _stringify2 = _interopRequireDefault(_stringify);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _superagent = __webpack_require__(/*! superagent */ "./node_modules/superagent/lib/client.js");

var _superagent2 = _interopRequireDefault(_superagent);

var _swaggerClient = __webpack_require__(/*! swagger-client */ "./node_modules/swagger-client/dist/index.js");

var _swaggerClient2 = _interopRequireDefault(_swaggerClient);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var REL_PATH = exports.REL_PATH = '/admin/';

var urls = {
  host: 'http://localhost:8000',
  metadata: '/admin/metadata/'
};

var Api = function () {
  function Api() {
    (0, _classCallCheck3.default)(this, Api);
  }

  (0, _createClass3.default)(Api, null, [{
    key: 'fetchMetadata',
    value: function fetchMetadata() {
      return _superagent2.default.get(urls.host + urls.metadata).then(function (response) {
        return response.body;
      }).catch(function (error) {
        throw Error(error.message);
      });
    }
  }, {
    key: 'fetchResource',
    value: function fetchResource(payload, client) {
      var resourceName = payload.resourceName,
          query = payload.query;

      return client.apis[resourceName].list(query).then(function (response) {
        return response.body;
      }).catch(function (error) {
        throw Error(error.message);
      });
    }
  }, {
    key: 'fetchResourceElement',
    value: function fetchResourceElement(payload, client) {
      var resource = payload.resourceName;
      var id = payload.resourceId;
      return client.apis[resource].retrieve({ element_id: id }).then(function (response) {
        return response.body;
      }).catch(function (error) {
        throw Error(error.message);
      });
    }
  }, {
    key: 'fetchSwaggerSchema',
    value: function fetchSwaggerSchema(schemaUrl) {
      return (0, _swaggerClient2.default)(urls.host + schemaUrl).then(function (client) {
        return client;
      });
    }
  }, {
    key: 'submitResource',
    value: function submitResource(payload, client) {
      return client.apis[payload.resourceName].create({}, { requestBody: payload.resourceData }).then(function (response) {
        return response.body;
      }).catch(function (error) {
        throw Error((0, _stringify2.default)(error.response.body));
      });
    }
  }, {
    key: 'updateResourceElement',
    value: function updateResourceElement(payload, client) {
      var resourceName = payload.resourceName,
          resourceId = payload.resourceId,
          resourceData = payload.resourceData;

      return client.apis[resourceName].update({ element_id: resourceId }, { requestBody: resourceData }).then(function (response) {
        return response.body;
      });
    }
  }, {
    key: 'deleteResourceElement',
    value: function deleteResourceElement(payload, client) {
      var resourceName = payload.resourceName,
          resourceId = payload.resourceId;

      return client.apis[resourceName].delete({ element_id: resourceId }).then(function (response) {
        return response.body;
      }).catch(function (error) {
        throw Error(error.message);
      });
    }
  }]);
  return Api;
}();

exports.default = Api;

/***/ }),

/***/ "./admin/components/Header/Header.js":
/*!*******************************************!*\
  !*** ./admin/components/Header/Header.js ***!
  \*******************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _getPrototypeOf = __webpack_require__(/*! babel-runtime/core-js/object/get-prototype-of */ "./node_modules/babel-runtime/core-js/object/get-prototype-of.js");

var _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _possibleConstructorReturn2 = __webpack_require__(/*! babel-runtime/helpers/possibleConstructorReturn */ "./node_modules/babel-runtime/helpers/possibleConstructorReturn.js");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = __webpack_require__(/*! babel-runtime/helpers/inherits */ "./node_modules/babel-runtime/helpers/inherits.js");

var _inherits3 = _interopRequireDefault(_inherits2);

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _core = __webpack_require__(/*! @material-ui/core */ "./node_modules/@material-ui/core/index.es.js");

var _reactRouterDom = __webpack_require__(/*! react-router-dom */ "./node_modules/react-router-dom/es/index.js");

var _reactRedux = __webpack_require__(/*! react-redux */ "./node_modules/react-redux/es/index.js");

var _styles = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/core/styles/index.js");

var _api = __webpack_require__(/*! ../../api */ "./admin/api.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var Header = function (_React$Component) {
  (0, _inherits3.default)(Header, _React$Component);

  function Header() {
    (0, _classCallCheck3.default)(this, Header);
    return (0, _possibleConstructorReturn3.default)(this, (Header.__proto__ || (0, _getPrototypeOf2.default)(Header)).apply(this, arguments));
  }

  (0, _createClass3.default)(Header, [{
    key: 'render',
    value: function render() {
      return _react2.default.createElement(
        _core.AppBar,
        { position: 'static' },
        _react2.default.createElement(
          _core.Toolbar,
          null,
          _react2.default.createElement(
            _core.Typography,
            { variant: 'title', color: 'inherit' },
            _react2.default.createElement(
              _reactRouterDom.Link,
              { to: _api.REL_PATH, className: 'HeaderLink' },
              'APISTAR'
            )
          )
        )
      );
    }
  }]);
  return Header;
}(_react2.default.Component);

var mapStateToProps = function mapStateToProps(state) {
  return {
    metadata: state.metadata
  };
};

exports.default = (0, _styles.withTheme)()((0, _reactRedux.connect)(mapStateToProps)(Header));

/***/ }),

/***/ "./admin/components/Header/index.js":
/*!******************************************!*\
  !*** ./admin/components/Header/index.js ***!
  \******************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _Header = __webpack_require__(/*! ./Header */ "./admin/components/Header/Header.js");

var _Header2 = _interopRequireDefault(_Header);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

exports.default = _Header2.default;

/***/ }),

/***/ "./admin/components/ResourceForm/ResourceForm.jsx":
/*!********************************************************!*\
  !*** ./admin/components/ResourceForm/ResourceForm.jsx ***!
  \********************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _entries = __webpack_require__(/*! babel-runtime/core-js/object/entries */ "./node_modules/babel-runtime/core-js/object/entries.js");

var _entries2 = _interopRequireDefault(_entries);

var _defineProperty2 = __webpack_require__(/*! babel-runtime/helpers/defineProperty */ "./node_modules/babel-runtime/helpers/defineProperty.js");

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _getPrototypeOf = __webpack_require__(/*! babel-runtime/core-js/object/get-prototype-of */ "./node_modules/babel-runtime/core-js/object/get-prototype-of.js");

var _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _possibleConstructorReturn2 = __webpack_require__(/*! babel-runtime/helpers/possibleConstructorReturn */ "./node_modules/babel-runtime/helpers/possibleConstructorReturn.js");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = __webpack_require__(/*! babel-runtime/helpers/inherits */ "./node_modules/babel-runtime/helpers/inherits.js");

var _inherits3 = _interopRequireDefault(_inherits2);

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _reactRedux = __webpack_require__(/*! react-redux */ "./node_modules/react-redux/es/index.js");

var _propTypes = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");

var _propTypes2 = _interopRequireDefault(_propTypes);

var _core = __webpack_require__(/*! @material-ui/core */ "./node_modules/@material-ui/core/index.es.js");

var _resource = __webpack_require__(/*! ../../ducks/resource */ "./admin/ducks/resource.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var propTypes = {
  schema: _propTypes2.default.object,
  setCurrentResourceElement: _propTypes2.default.func,
  updateResourceElement: _propTypes2.default.func,
  submitResource: _propTypes2.default.func,
  deleteResourceElement: _propTypes2.default.func,
  resourceId: _propTypes2.default.string,
  resourceName: _propTypes2.default.string,
  currentResourceElement: _propTypes2.default.object
};
var defaultProps = {};

var typeMaps = {
  string: 'text',
  integer: 'number',
  float: 'number', // TODO: fix
  datetime: 'datetime' // TODO: fix
};

var ResourceForm = function (_React$Component) {
  (0, _inherits3.default)(ResourceForm, _React$Component);

  function ResourceForm() {
    (0, _classCallCheck3.default)(this, ResourceForm);

    var _this = (0, _possibleConstructorReturn3.default)(this, (ResourceForm.__proto__ || (0, _getPrototypeOf2.default)(ResourceForm)).call(this));

    _this.handleInputChange = _this.handleInputChange.bind(_this);
    _this.handleSubmit = _this.handleSubmit.bind(_this);
    _this.handleDialogClose = _this.handleDialogClose.bind(_this);
    _this.handleDialogOpen = _this.handleDialogOpen.bind(_this);
    _this.handleDeleteConfirmClick = _this.handleDeleteConfirmClick.bind(_this);
    _this.state = { data: null, isDialogOpen: false };
    return _this;
  }

  (0, _createClass3.default)(ResourceForm, [{
    key: 'handleInputChange',
    value: function handleInputChange(evt) {
      var _evt$target = evt.target,
          name = _evt$target.name,
          value = _evt$target.value;

      this.props.setCurrentResourceElement((0, _defineProperty3.default)({}, name, value));
    }
  }, {
    key: 'handleSubmit',
    value: function handleSubmit(evt) {
      evt.preventDefault();
      if (this.props.resourceId !== 'new') {
        this.props.updateResourceElement({
          resourceName: this.props.resourceName,
          resourceData: this.props.currentResourceElement,
          resourceId: this.props.resourceId
        });
      } else {
        this.props.submitResource({
          resourceName: this.props.resourceName,
          resourceData: this.props.currentResourceElement
        });
      }
    }
  }, {
    key: 'handleDialogClose',
    value: function handleDialogClose() {
      this.setState({ isDialogOpen: false });
    }
  }, {
    key: 'handleDialogOpen',
    value: function handleDialogOpen() {
      this.setState({ isDialogOpen: true });
    }
  }, {
    key: 'handleDeleteConfirmClick',
    value: function handleDeleteConfirmClick() {
      this.props.deleteResourceElement({
        resourceName: this.props.resourceName,
        resourceId: this.props.resourceId
      });
    }
  }, {
    key: 'render',
    value: function render() {
      var _this2 = this;

      var data = this.props.currentResourceElement;
      var errors = this.props.errors;
      var resourceSchema = this.props.schema && this.props.schema.spec.paths['/' + this.props.resourceName + '/'].post.requestBody.content['application/json'].schema;
      var requiredFields = resourceSchema && resourceSchema.required;
      return resourceSchema ? _react2.default.createElement(
        'form',
        { action: '', onSubmit: this.handleSubmit },
        _react2.default.createElement(
          _core.Grid,
          { container: true, alignItems: 'center', justify: 'center' },
          _react2.default.createElement(
            _core.Grid,
            { item: true, xs: 12, sm: 5 },
            (0, _entries2.default)(resourceSchema.properties).map(function (field) {
              return _react2.default.createElement(_core.TextField, {
                key: field[1].title,
                error: errors && (field[1].title ? !!errors[field[1].title] : !!errors[field[0]]),
                type: typeMaps[field[1].type] || 'text',
                min: field[1].minimum,
                max: field[1].maximum,
                id: field[1].title || field[0],
                label: field[1].description,
                name: field[1].title || field[0],
                value: data && (data[field[1].title] || data[field[0]]) || '',
                onChange: _this2.handleInputChange,
                margin: 'normal',
                fullWidth: true,
                required: requiredFields.includes(field[0]),
                helperText: errors && (field[1].title ? errors[field[1].title] : errors[field[0]]) || null
              });
            }),
            this.props.resourceId !== 'new' && _react2.default.createElement(
              _core.Button,
              {
                variant: 'contained',
                color: 'secondary',
                className: 'ButtonDelete',
                onClick: this.handleDialogOpen
              },
              'Delete'
            ),
            _react2.default.createElement(
              _core.Button,
              {
                variant: 'contained',
                color: 'primary',
                type: 'submit',
                className: 'ButtonSave'
              },
              'Save'
            ),
            _react2.default.createElement(
              _core.Dialog,
              {
                open: this.state.isDialogOpen,
                onClose: this.handleDialogClose,
                'aria-labelledby': 'alert-dialog-title',
                'aria-describedby': 'alert-dialog-description'
              },
              _react2.default.createElement(
                _core.DialogTitle,
                { id: 'alert-dialog-title' },
                'Confirm'
              ),
              _react2.default.createElement(
                _core.DialogContent,
                null,
                _react2.default.createElement(
                  _core.DialogContentText,
                  { id: 'alert-dialog-description' },
                  'Are you sure you want to delete this item?'
                )
              ),
              _react2.default.createElement(
                _core.DialogActions,
                null,
                _react2.default.createElement(
                  _core.Button,
                  {
                    onClick: this.handleDeleteConfirmClick,
                    color: 'secondary',
                    variant: 'contained',
                    autoFocus: true
                  },
                  'Yes, Delete.'
                ),
                _react2.default.createElement(
                  _core.Button,
                  { onClick: this.handleDialogClose },
                  'Cancel'
                )
              )
            )
          )
        )
      ) : _react2.default.createElement(
        'div',
        { className: 'SpinnerContainer' },
        _react2.default.createElement(_core.CircularProgress, null)
      );
    }
  }]);
  return ResourceForm;
}(_react2.default.Component);

ResourceForm.propTypes = propTypes;
ResourceForm.defaultProps = defaultProps;

var mapStateToProps = function mapStateToProps(state) {
  return {
    resources: state.resource.entities,
    schema: state.metadata.client,
    currentResourceElement: state.resource.currentResourceElement,
    errors: state.resource.errors
  };
};

var mapDispatchToProps = {
  submitResource: _resource.submitResourceRequest,
  setCurrentResourceElement: _resource.setCurrentResourceElement,
  updateResourceElement: _resource.updateResourceElementRequest,
  deleteResourceElement: _resource.deleteResourceElementRequest
};

exports.default = (0, _reactRedux.connect)(mapStateToProps, mapDispatchToProps)(ResourceForm);

/***/ }),

/***/ "./admin/components/ResourceForm/index.js":
/*!************************************************!*\
  !*** ./admin/components/ResourceForm/index.js ***!
  \************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _ResourceForm = __webpack_require__(/*! ./ResourceForm */ "./admin/components/ResourceForm/ResourceForm.jsx");

var _ResourceForm2 = _interopRequireDefault(_ResourceForm);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

exports.default = _ResourceForm2.default;

/***/ }),

/***/ "./admin/components/TablePaginationActions/TablePaginationActions.jsx":
/*!****************************************************************************!*\
  !*** ./admin/components/TablePaginationActions/TablePaginationActions.jsx ***!
  \****************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _getPrototypeOf = __webpack_require__(/*! babel-runtime/core-js/object/get-prototype-of */ "./node_modules/babel-runtime/core-js/object/get-prototype-of.js");

var _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _possibleConstructorReturn2 = __webpack_require__(/*! babel-runtime/helpers/possibleConstructorReturn */ "./node_modules/babel-runtime/helpers/possibleConstructorReturn.js");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = __webpack_require__(/*! babel-runtime/helpers/inherits */ "./node_modules/babel-runtime/helpers/inherits.js");

var _inherits3 = _interopRequireDefault(_inherits2);

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _propTypes = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");

var _propTypes2 = _interopRequireDefault(_propTypes);

var _core = __webpack_require__(/*! @material-ui/core */ "./node_modules/@material-ui/core/index.es.js");

var _icons = __webpack_require__(/*! @material-ui/icons/ */ "./node_modules/@material-ui/icons/index.es.js");

var _FirstPage = __webpack_require__(/*! @material-ui/icons/FirstPage */ "./node_modules/@material-ui/icons/FirstPage.js");

var _FirstPage2 = _interopRequireDefault(_FirstPage);

var _LastPage = __webpack_require__(/*! @material-ui/icons/LastPage */ "./node_modules/@material-ui/icons/LastPage.js");

var _LastPage2 = _interopRequireDefault(_LastPage);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var propTypes = {
  onChangePage: _propTypes2.default.func,
  rowsPerPage: _propTypes2.default.number,
  count: _propTypes2.default.number,
  page: _propTypes2.default.number
};

var TablePaginationActions = function (_React$Component) {
  (0, _inherits3.default)(TablePaginationActions, _React$Component);

  function TablePaginationActions() {
    (0, _classCallCheck3.default)(this, TablePaginationActions);

    var _this = (0, _possibleConstructorReturn3.default)(this, (TablePaginationActions.__proto__ || (0, _getPrototypeOf2.default)(TablePaginationActions)).call(this));

    _this.handleBackButtonClick = _this.handleBackButtonClick.bind(_this);
    _this.handleFirstPageButtonClick = _this.handleFirstPageButtonClick.bind(_this);
    _this.handleNextButtonClick = _this.handleNextButtonClick.bind(_this);
    _this.handleLastPageButtonClick = _this.handleLastPageButtonClick.bind(_this);
    return _this;
  }

  (0, _createClass3.default)(TablePaginationActions, [{
    key: 'handleFirstPageButtonClick',
    value: function handleFirstPageButtonClick(event) {
      this.props.onChangePage(event, 0);
    }
  }, {
    key: 'handleBackButtonClick',
    value: function handleBackButtonClick(event) {
      this.props.onChangePage(event, this.props.page - 1);
    }
  }, {
    key: 'handleNextButtonClick',
    value: function handleNextButtonClick(event) {
      this.props.onChangePage(event, this.props.page + 1);
    }
  }, {
    key: 'handleLastPageButtonClick',
    value: function handleLastPageButtonClick(event) {
      this.props.onChangePage(event, Math.max(0, Math.ceil(this.props.count / this.props.rowsPerPage) - 1));
    }
  }, {
    key: 'render',
    value: function render() {
      var _props = this.props,
          count = _props.count,
          page = _props.page,
          rowsPerPage = _props.rowsPerPage;

      return _react2.default.createElement(
        'div',
        { className: 'TableActions' },
        _react2.default.createElement(
          _core.IconButton,
          {
            onClick: this.handleFirstPageButtonClick,
            disabled: page === 0,
            'aria-label': 'First Page'
          },
          _react2.default.createElement(_FirstPage2.default, null)
        ),
        _react2.default.createElement(
          _core.IconButton,
          {
            onClick: this.handleBackButtonClick,
            disabled: page === 0,
            'aria-label': 'Previous Page'
          },
          _react2.default.createElement(_icons.KeyboardArrowLeft, null)
        ),
        _react2.default.createElement(
          _core.IconButton,
          {
            onClick: this.handleNextButtonClick,
            disabled: page >= Math.ceil(count / rowsPerPage) - 1,
            'aria-label': 'Next Page'
          },
          _react2.default.createElement(_icons.KeyboardArrowRight, null)
        ),
        _react2.default.createElement(
          _core.IconButton,
          {
            onClick: this.handleLastPageButtonClick,
            disabled: page >= Math.ceil(count / rowsPerPage) - 1,
            'aria-label': 'Last Page'
          },
          _react2.default.createElement(_LastPage2.default, null)
        )
      );
    }
  }]);
  return TablePaginationActions;
}(_react2.default.Component);

TablePaginationActions.propTypes = propTypes;

exports.default = TablePaginationActions;

/***/ }),

/***/ "./admin/components/TablePaginationActions/index.jsx":
/*!***********************************************************!*\
  !*** ./admin/components/TablePaginationActions/index.jsx ***!
  \***********************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _TablePaginationActions = __webpack_require__(/*! ./TablePaginationActions */ "./admin/components/TablePaginationActions/TablePaginationActions.jsx");

var _TablePaginationActions2 = _interopRequireDefault(_TablePaginationActions);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

exports.default = _TablePaginationActions2.default;

/***/ }),

/***/ "./admin/ducks/index.js":
/*!******************************!*\
  !*** ./admin/ducks/index.js ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _redux = __webpack_require__(/*! redux */ "./node_modules/redux/es/index.js");

var _metadata = __webpack_require__(/*! ./metadata */ "./admin/ducks/metadata.js");

var _metadata2 = _interopRequireDefault(_metadata);

var _resource = __webpack_require__(/*! ./resource */ "./admin/ducks/resource.js");

var _resource2 = _interopRequireDefault(_resource);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

exports.default = (0, _redux.combineReducers)({
  metadata: _metadata2.default,
  resource: _resource2.default
});

/***/ }),

/***/ "./admin/ducks/metadata.js":
/*!*********************************!*\
  !*** ./admin/ducks/metadata.js ***!
  \*********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.fetchMetadataFailure = exports.fetchMetadataSuccess = exports.fetchMetadataRequest = exports.FETCH_METADATA_FAILURE = exports.FETCH_METADATA_SUCCESS = exports.FETCH_METADATA_REQUEST = undefined;

var _defineProperty2 = __webpack_require__(/*! babel-runtime/helpers/defineProperty */ "./node_modules/babel-runtime/helpers/defineProperty.js");

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _extends2 = __webpack_require__(/*! babel-runtime/helpers/extends */ "./node_modules/babel-runtime/helpers/extends.js");

var _extends3 = _interopRequireDefault(_extends2);

var _handleActions;

var _reduxActions = __webpack_require__(/*! redux-actions */ "./node_modules/redux-actions/es/index.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var FETCH_METADATA_REQUEST = exports.FETCH_METADATA_REQUEST = 'metadata/fetch/REQUEST';
var FETCH_METADATA_SUCCESS = exports.FETCH_METADATA_SUCCESS = 'metadata/fetch/SUCCESS';
var FETCH_METADATA_FAILURE = exports.FETCH_METADATA_FAILURE = 'metadata/fetch/FAILURE';

var fetchMetadataRequest = exports.fetchMetadataRequest = (0, _reduxActions.createAction)(FETCH_METADATA_REQUEST);
var fetchMetadataSuccess = exports.fetchMetadataSuccess = (0, _reduxActions.createAction)(FETCH_METADATA_SUCCESS);
var fetchMetadataFailure = exports.fetchMetadataFailure = (0, _reduxActions.createAction)(FETCH_METADATA_FAILURE);

var initialState = {
  resources: null,
  schema: null,
  client: null
};

exports.default = (0, _reduxActions.handleActions)((_handleActions = {}, (0, _defineProperty3.default)(_handleActions, FETCH_METADATA_SUCCESS, function (state, _ref) {
  var payload = _ref.payload;
  return (0, _extends3.default)({}, state, {
    resources: payload.resources,
    schema: payload.schema,
    client: payload.client
  });
}), (0, _defineProperty3.default)(_handleActions, FETCH_METADATA_FAILURE, function (state, _ref2) {
  var payload = _ref2.payload;
  return (0, _extends3.default)({}, state, {
    error: payload
  });
}), _handleActions), initialState);

/***/ }),

/***/ "./admin/ducks/resource.js":
/*!*********************************!*\
  !*** ./admin/ducks/resource.js ***!
  \*********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.deleteResourceElementRequest = exports.setCurrentResourceElement = exports.updateResourceElementFailure = exports.updateResourceElementSuccess = exports.updateResourceElementRequest = exports.submitResourceFailure = exports.submitResourceSuccess = exports.submitResourceRequest = exports.fetchCurrentResourceSuccess = exports.fetchCurrentResourceRequest = exports.fetchResourceEntitiesSuccess = exports.fetchResourceEntitiesRequest = exports.DELETE_RESOURCE_ELEMENT_REQUEST = exports.SET_CURRENT_RESOURCE_ELEMENT = exports.UPDATE_RESOURCE_ELEMENT_FAILURE = exports.UPDATE_RESOURCE_ELEMENT_SUCCESS = exports.UPDATE_RESOURCE_ELEMENT_REQUEST = exports.SUBMIT_RESOURCE_FAILURE = exports.SUBMIT_RESOURCE_SUCCESS = exports.SUBMIT_RESOURCE_REQUEST = exports.FETCH_CURRENT_RESOURCE_FAILURE = exports.FETCH_CURRENT_RESOURCE_SUCCESS = exports.FETCH_CURRENT_RESOURCE_REQUEST = exports.FETCH_RESOURCE_ENTITIES_FAILURE = exports.FETCH_RESOURCE_ENTITIES_SUCCESS = exports.FETCH_RESOURCE_ENTITIES_REQUEST = undefined;

var _defineProperty2 = __webpack_require__(/*! babel-runtime/helpers/defineProperty */ "./node_modules/babel-runtime/helpers/defineProperty.js");

var _defineProperty3 = _interopRequireDefault(_defineProperty2);

var _toConsumableArray2 = __webpack_require__(/*! babel-runtime/helpers/toConsumableArray */ "./node_modules/babel-runtime/helpers/toConsumableArray.js");

var _toConsumableArray3 = _interopRequireDefault(_toConsumableArray2);

var _extends2 = __webpack_require__(/*! babel-runtime/helpers/extends */ "./node_modules/babel-runtime/helpers/extends.js");

var _extends3 = _interopRequireDefault(_extends2);

var _handleActions;

var _reduxActions = __webpack_require__(/*! redux-actions */ "./node_modules/redux-actions/es/index.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var FETCH_RESOURCE_ENTITIES_REQUEST = exports.FETCH_RESOURCE_ENTITIES_REQUEST = 'resource/entities/fetch/REQUEST';
var FETCH_RESOURCE_ENTITIES_SUCCESS = exports.FETCH_RESOURCE_ENTITIES_SUCCESS = 'resource/entities/fetch/SUCCESS';
var FETCH_RESOURCE_ENTITIES_FAILURE = exports.FETCH_RESOURCE_ENTITIES_FAILURE = 'resource/entities/fetch/FAILURE';

var FETCH_CURRENT_RESOURCE_REQUEST = exports.FETCH_CURRENT_RESOURCE_REQUEST = 'resource/current-resource/REQUEST';
var FETCH_CURRENT_RESOURCE_SUCCESS = exports.FETCH_CURRENT_RESOURCE_SUCCESS = 'resource/current-resource/SUCCESS';
var FETCH_CURRENT_RESOURCE_FAILURE = exports.FETCH_CURRENT_RESOURCE_FAILURE = 'resource/current-resource/FAILURE';

var SUBMIT_RESOURCE_REQUEST = exports.SUBMIT_RESOURCE_REQUEST = 'resource/submit/REQUEST';
var SUBMIT_RESOURCE_SUCCESS = exports.SUBMIT_RESOURCE_SUCCESS = 'resource/submit/SUCCESS';
var SUBMIT_RESOURCE_FAILURE = exports.SUBMIT_RESOURCE_FAILURE = 'resource/submit/FAILURE';

var UPDATE_RESOURCE_ELEMENT_REQUEST = exports.UPDATE_RESOURCE_ELEMENT_REQUEST = 'resource/update/REQUEST';
var UPDATE_RESOURCE_ELEMENT_SUCCESS = exports.UPDATE_RESOURCE_ELEMENT_SUCCESS = 'resource/update/SUCCESS';
var UPDATE_RESOURCE_ELEMENT_FAILURE = exports.UPDATE_RESOURCE_ELEMENT_FAILURE = 'resource/update/FAILURE';

var SET_CURRENT_RESOURCE_ELEMENT = exports.SET_CURRENT_RESOURCE_ELEMENT = 'resource/current-resource/SET';

var DELETE_RESOURCE_ELEMENT_REQUEST = exports.DELETE_RESOURCE_ELEMENT_REQUEST = 'resource/delete/REQUEST';

var fetchResourceEntitiesRequest = exports.fetchResourceEntitiesRequest = (0, _reduxActions.createAction)(FETCH_RESOURCE_ENTITIES_REQUEST);
var fetchResourceEntitiesSuccess = exports.fetchResourceEntitiesSuccess = (0, _reduxActions.createAction)(FETCH_RESOURCE_ENTITIES_SUCCESS);
var fetchCurrentResourceRequest = exports.fetchCurrentResourceRequest = (0, _reduxActions.createAction)(FETCH_CURRENT_RESOURCE_REQUEST);
var fetchCurrentResourceSuccess = exports.fetchCurrentResourceSuccess = (0, _reduxActions.createAction)(FETCH_CURRENT_RESOURCE_SUCCESS);

var submitResourceRequest = exports.submitResourceRequest = (0, _reduxActions.createAction)(SUBMIT_RESOURCE_REQUEST);
var submitResourceSuccess = exports.submitResourceSuccess = (0, _reduxActions.createAction)(SUBMIT_RESOURCE_SUCCESS);
var submitResourceFailure = exports.submitResourceFailure = (0, _reduxActions.createAction)(SUBMIT_RESOURCE_FAILURE);
var updateResourceElementRequest = exports.updateResourceElementRequest = (0, _reduxActions.createAction)(UPDATE_RESOURCE_ELEMENT_REQUEST);
var updateResourceElementSuccess = exports.updateResourceElementSuccess = (0, _reduxActions.createAction)(UPDATE_RESOURCE_ELEMENT_SUCCESS);
var updateResourceElementFailure = exports.updateResourceElementFailure = (0, _reduxActions.createAction)(UPDATE_RESOURCE_ELEMENT_FAILURE);
var setCurrentResourceElement = exports.setCurrentResourceElement = (0, _reduxActions.createAction)(SET_CURRENT_RESOURCE_ELEMENT);

var deleteResourceElementRequest = exports.deleteResourceElementRequest = (0, _reduxActions.createAction)(DELETE_RESOURCE_ELEMENT_REQUEST);

var initialState = {
  entities: null,
  currentResourceElement: null,
  rowsPerPage: null,
  totalCount: null,
  currentPage: null,
  errors: null
};

exports.default = (0, _reduxActions.handleActions)((_handleActions = {}, (0, _defineProperty3.default)(_handleActions, FETCH_RESOURCE_ENTITIES_SUCCESS, function (state, _ref) {
  var payload = _ref.payload;
  return (0, _extends3.default)({}, state, {
    entities: payload.resources.data,
    currentResourceElement: null,
    rowsPerPage: payload.resources.meta.page_size,
    currentPage: payload.resources.meta.page,
    totalCount: payload.resources.meta.count
  });
}), (0, _defineProperty3.default)(_handleActions, FETCH_CURRENT_RESOURCE_SUCCESS, function (state, _ref2) {
  var payload = _ref2.payload;
  return (0, _extends3.default)({}, state, {
    currentResourceElement: payload
  });
}), (0, _defineProperty3.default)(_handleActions, SUBMIT_RESOURCE_SUCCESS, function (state, _ref3) {
  var payload = _ref3.payload;
  return (0, _extends3.default)({}, state, {
    entities: [].concat((0, _toConsumableArray3.default)(state.entities), [payload])
  });
}), (0, _defineProperty3.default)(_handleActions, SUBMIT_RESOURCE_FAILURE, function (state, _ref4) {
  var payload = _ref4.payload;
  return (0, _extends3.default)({}, state, {
    errors: payload
  });
}), (0, _defineProperty3.default)(_handleActions, SET_CURRENT_RESOURCE_ELEMENT, function (state, _ref5) {
  var payload = _ref5.payload;
  return (0, _extends3.default)({}, state, {
    currentResourceElement: (0, _extends3.default)({}, state.currentResourceElement, payload)
  });
}), _handleActions), initialState);

/***/ }),

/***/ "./admin/index.js":
/*!************************!*\
  !*** ./admin/index.js ***!
  \************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.history = undefined;

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _reactDom = __webpack_require__(/*! react-dom */ "./node_modules/react-dom/index.js");

var _reactDom2 = _interopRequireDefault(_reactDom);

var _AppContainer = __webpack_require__(/*! ./AppContainer */ "./admin/AppContainer.js");

var _AppContainer2 = _interopRequireDefault(_AppContainer);

__webpack_require__(/*! ./index.css */ "./admin/index.css");

var _createBrowserHistory = __webpack_require__(/*! history/createBrowserHistory */ "./node_modules/history/createBrowserHistory.js");

var _createBrowserHistory2 = _interopRequireDefault(_createBrowserHistory);

var _reactRedux = __webpack_require__(/*! react-redux */ "./node_modules/react-redux/es/index.js");

var _redux = __webpack_require__(/*! redux */ "./node_modules/redux/es/index.js");

var _connectedReactRouter = __webpack_require__(/*! connected-react-router */ "./node_modules/connected-react-router/lib/index.js");

var _reduxSaga = __webpack_require__(/*! redux-saga */ "./node_modules/redux-saga/es/index.js");

var _reduxSaga2 = _interopRequireDefault(_reduxSaga);

var _ducks = __webpack_require__(/*! ./ducks */ "./admin/ducks/index.js");

var _ducks2 = _interopRequireDefault(_ducks);

var _sagas = __webpack_require__(/*! ./sagas */ "./admin/sagas/index.js");

var _sagas2 = _interopRequireDefault(_sagas);

var _reactTapEventPlugin = __webpack_require__(/*! react-tap-event-plugin */ "./node_modules/react-tap-event-plugin/src/injectTapEventPlugin.js");

var _reactTapEventPlugin2 = _interopRequireDefault(_reactTapEventPlugin);

var _styles = __webpack_require__(/*! @material-ui/core/styles/ */ "./node_modules/@material-ui/core/styles/index.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var muiTheme = (0, _styles.createMuiTheme)({
  palette: {
    primary: { main: '#31CACC', contrastText: '#fff' }
  }
});

var history = exports.history = (0, _createBrowserHistory2.default)();
var sagaMiddleware = (0, _reduxSaga2.default)();

var composeEnhancers = _redux.compose;

if (true) {
  var composeWithDevToolsExtension = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__;
  if (typeof composeWithDevToolsExtension === 'function') {
    composeEnhancers = composeWithDevToolsExtension;
  }
}

var store = (0, _redux.createStore)((0, _connectedReactRouter.connectRouter)(history)(_ducks2.default), composeEnhancers((0, _redux.applyMiddleware)((0, _connectedReactRouter.routerMiddleware)(history), sagaMiddleware)));

sagaMiddleware.run(_sagas2.default);

(0, _reactTapEventPlugin2.default)();

_reactDom2.default.render(_react2.default.createElement(
  _styles.MuiThemeProvider,
  { theme: muiTheme },
  _react2.default.createElement(
    _reactRedux.Provider,
    { store: store },
    _react2.default.createElement(_AppContainer2.default, null)
  )
), document.getElementById('root'));

/***/ }),

/***/ "./admin/routes/DetailPage.jsx":
/*!*************************************!*\
  !*** ./admin/routes/DetailPage.jsx ***!
  \*************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = __webpack_require__(/*! babel-runtime/helpers/extends */ "./node_modules/babel-runtime/helpers/extends.js");

var _extends3 = _interopRequireDefault(_extends2);

var _getPrototypeOf = __webpack_require__(/*! babel-runtime/core-js/object/get-prototype-of */ "./node_modules/babel-runtime/core-js/object/get-prototype-of.js");

var _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _possibleConstructorReturn2 = __webpack_require__(/*! babel-runtime/helpers/possibleConstructorReturn */ "./node_modules/babel-runtime/helpers/possibleConstructorReturn.js");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = __webpack_require__(/*! babel-runtime/helpers/inherits */ "./node_modules/babel-runtime/helpers/inherits.js");

var _inherits3 = _interopRequireDefault(_inherits2);

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _reactRedux = __webpack_require__(/*! react-redux */ "./node_modules/react-redux/es/index.js");

var _reactRouterDom = __webpack_require__(/*! react-router-dom */ "./node_modules/react-router-dom/es/index.js");

var _propTypes = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");

var _propTypes2 = _interopRequireDefault(_propTypes);

var _core = __webpack_require__(/*! @material-ui/core */ "./node_modules/@material-ui/core/index.es.js");

var _api = __webpack_require__(/*! ../api */ "./admin/api.js");

var _ResourceForm = __webpack_require__(/*! ../components/ResourceForm */ "./admin/components/ResourceForm/index.js");

var _ResourceForm2 = _interopRequireDefault(_ResourceForm);

var _resource = __webpack_require__(/*! ../ducks/resource */ "./admin/ducks/resource.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var propTypes = {
  metadata: _propTypes2.default.shape({
    resources: _propTypes2.default.object,
    client: _propTypes2.default.object,
    schema: _propTypes2.default.string
  }),
  match: _propTypes2.default.object,
  fetchResource: _propTypes2.default.func.isRequired
};

var DetailPage = function (_React$Component) {
  (0, _inherits3.default)(DetailPage, _React$Component);

  function DetailPage() {
    (0, _classCallCheck3.default)(this, DetailPage);
    return (0, _possibleConstructorReturn3.default)(this, (DetailPage.__proto__ || (0, _getPrototypeOf2.default)(DetailPage)).apply(this, arguments));
  }

  (0, _createClass3.default)(DetailPage, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      if (this.props.match.params.id !== 'new') {
        this.props.fetchResource({
          resourceName: this.props.match.params.resource,
          resourceId: this.props.match.params.id
        });
      }
    }
  }, {
    key: 'render',
    value: function render() {
      var resourceName = this.props.match.params.resource;
      var resourceId = this.props.match.params.id;

      return _react2.default.createElement(
        _core.Grid,
        { container: true, className: 'MainContainer' },
        _react2.default.createElement(
          _core.Grid,
          { item: true, xs: 12 },
          _react2.default.createElement(
            _core.Button,
            {
              className: 'ButtonBack',
              component: function component(props) {
                return _react2.default.createElement(_reactRouterDom.Link, (0, _extends3.default)({ to: '' + _api.REL_PATH + resourceName + '/' }, props));
              }
            },
            _react2.default.createElement(
              _core.Icon,
              null,
              'arrow_back'
            ),
            '\xA0Back'
          ),
          _react2.default.createElement(_ResourceForm2.default, { resourceName: resourceName, resourceId: resourceId })
        )
      );
    }
  }]);
  return DetailPage;
}(_react2.default.Component);

DetailPage.propTypes = propTypes;

var mapStateToProps = function mapStateToProps(state) {
  return {
    metadata: state.metadata
  };
};

var mapDispatchToProps = {
  fetchResource: _resource.fetchCurrentResourceRequest
};

exports.default = (0, _reactRedux.connect)(mapStateToProps, mapDispatchToProps)(DetailPage);

/***/ }),

/***/ "./admin/routes/ErrorPage.jsx":
/*!************************************!*\
  !*** ./admin/routes/ErrorPage.jsx ***!
  \************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _propTypes = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");

var _propTypes2 = _interopRequireDefault(_propTypes);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var propTypes = {};
var defaultProps = {};

var ErrorPage = function ErrorPage(props) {
  return _react2.default.createElement(
    'div',
    null,
    '404 Not found'
  );
};

ErrorPage.propTypes = propTypes;
ErrorPage.defaultProps = defaultProps;

exports.default = ErrorPage;

/***/ }),

/***/ "./admin/routes/HomePage.js":
/*!**********************************!*\
  !*** ./admin/routes/HomePage.js ***!
  \**********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends2 = __webpack_require__(/*! babel-runtime/helpers/extends */ "./node_modules/babel-runtime/helpers/extends.js");

var _extends3 = _interopRequireDefault(_extends2);

var _entries = __webpack_require__(/*! babel-runtime/core-js/object/entries */ "./node_modules/babel-runtime/core-js/object/entries.js");

var _entries2 = _interopRequireDefault(_entries);

var _getPrototypeOf = __webpack_require__(/*! babel-runtime/core-js/object/get-prototype-of */ "./node_modules/babel-runtime/core-js/object/get-prototype-of.js");

var _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _possibleConstructorReturn2 = __webpack_require__(/*! babel-runtime/helpers/possibleConstructorReturn */ "./node_modules/babel-runtime/helpers/possibleConstructorReturn.js");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = __webpack_require__(/*! babel-runtime/helpers/inherits */ "./node_modules/babel-runtime/helpers/inherits.js");

var _inherits3 = _interopRequireDefault(_inherits2);

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _reactRedux = __webpack_require__(/*! react-redux */ "./node_modules/react-redux/es/index.js");

var _reactRouterDom = __webpack_require__(/*! react-router-dom */ "./node_modules/react-router-dom/es/index.js");

var _propTypes = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");

var _propTypes2 = _interopRequireDefault(_propTypes);

var _core = __webpack_require__(/*! @material-ui/core */ "./node_modules/@material-ui/core/index.es.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var propTypes = {
  metadata: _propTypes2.default.shape({
    resources: _propTypes2.default.object,
    schema: _propTypes2.default.string,
    client: _propTypes2.default.object
  })
};

var HomePage = function (_React$Component) {
  (0, _inherits3.default)(HomePage, _React$Component);

  function HomePage() {
    (0, _classCallCheck3.default)(this, HomePage);
    return (0, _possibleConstructorReturn3.default)(this, (HomePage.__proto__ || (0, _getPrototypeOf2.default)(HomePage)).apply(this, arguments));
  }

  (0, _createClass3.default)(HomePage, [{
    key: 'render',
    value: function render() {
      var resources = this.props.metadata.resources;

      return resources && _react2.default.createElement(
        _core.Grid,
        { container: true, alignItems: 'center', className: 'MainContainer' },
        _react2.default.createElement(
          _core.Grid,
          { item: true, xs: 12, sm: 6 },
          _react2.default.createElement(
            _core.Paper,
            { square: true },
            _react2.default.createElement(
              _core.Typography,
              { variant: 'title', className: 'PanelTitle' },
              'Resources'
            ),
            _react2.default.createElement(
              _core.List,
              { component: 'nav' },
              (0, _entries2.default)(resources).map(function (resource) {
                return _react2.default.createElement(
                  _core.ListItem,
                  {
                    key: resource[0],
                    button: true,
                    component: function component(props) {
                      return _react2.default.createElement(_reactRouterDom.Link, (0, _extends3.default)({ to: resource[1] + '/' }, props));
                    }
                  },
                  _react2.default.createElement(_core.ListItemText, { primary: resource[0] })
                );
              })
            )
          )
        )
      );
    }
  }]);
  return HomePage;
}(_react2.default.Component);

HomePage.propTypes = propTypes;

var mapStateToProps = function mapStateToProps(state) {
  return {
    metadata: state.metadata
  };
};

exports.default = (0, _reactRedux.connect)(mapStateToProps)(HomePage);

/***/ }),

/***/ "./admin/routes/ListPage.jsx":
/*!***********************************!*\
  !*** ./admin/routes/ListPage.jsx ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _values = __webpack_require__(/*! babel-runtime/core-js/object/values */ "./node_modules/babel-runtime/core-js/object/values.js");

var _values2 = _interopRequireDefault(_values);

var _extends2 = __webpack_require__(/*! babel-runtime/helpers/extends */ "./node_modules/babel-runtime/helpers/extends.js");

var _extends3 = _interopRequireDefault(_extends2);

var _getPrototypeOf = __webpack_require__(/*! babel-runtime/core-js/object/get-prototype-of */ "./node_modules/babel-runtime/core-js/object/get-prototype-of.js");

var _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _possibleConstructorReturn2 = __webpack_require__(/*! babel-runtime/helpers/possibleConstructorReturn */ "./node_modules/babel-runtime/helpers/possibleConstructorReturn.js");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = __webpack_require__(/*! babel-runtime/helpers/inherits */ "./node_modules/babel-runtime/helpers/inherits.js");

var _inherits3 = _interopRequireDefault(_inherits2);

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _propTypes = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");

var _propTypes2 = _interopRequireDefault(_propTypes);

var _reactRedux = __webpack_require__(/*! react-redux */ "./node_modules/react-redux/es/index.js");

var _findKey = __webpack_require__(/*! lodash/findKey */ "./node_modules/lodash/findKey.js");

var _findKey2 = _interopRequireDefault(_findKey);

var _core = __webpack_require__(/*! @material-ui/core */ "./node_modules/@material-ui/core/index.es.js");

var _reactRouterDom = __webpack_require__(/*! react-router-dom */ "./node_modules/react-router-dom/es/index.js");

var _api = __webpack_require__(/*! ../api */ "./admin/api.js");

var _TablePaginationActions = __webpack_require__(/*! ../components/TablePaginationActions */ "./admin/components/TablePaginationActions/index.jsx");

var _TablePaginationActions2 = _interopRequireDefault(_TablePaginationActions);

var _resource = __webpack_require__(/*! ../ducks/resource */ "./admin/ducks/resource.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var propTypes = {
  match: _propTypes2.default.object,
  fetchResources: _propTypes2.default.func,
  schema: _propTypes2.default.PropTypes.object,
  resources: _propTypes2.default.arrayOf(_propTypes2.default.object),
  rowsPerPage: _propTypes2.default.number,
  currentPage: _propTypes2.default.number
};

var DEFAULT_PAGE_SIZE = 10;

var ListPage = function (_React$Component) {
  (0, _inherits3.default)(ListPage, _React$Component);

  function ListPage() {
    (0, _classCallCheck3.default)(this, ListPage);

    var _this = (0, _possibleConstructorReturn3.default)(this, (ListPage.__proto__ || (0, _getPrototypeOf2.default)(ListPage)).call(this));

    _this.handleChangePage = _this.handleChangePage.bind(_this);
    return _this;
  }

  (0, _createClass3.default)(ListPage, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      this.props.fetchResources({
        resourceName: this.props.match.params.resource,
        query: {
          page_size: DEFAULT_PAGE_SIZE,
          page: 1
        }
      });
    }
  }, {
    key: 'handleChangePage',
    value: function handleChangePage(evt, page) {
      // Mui has some weird default pagination behaviour on cDU
      if (evt) {
        this.props.fetchResources({
          resourceName: this.props.match.params.resource,
          query: {
            page: page + 1, // TablePagination starts at 0;
            page_size: DEFAULT_PAGE_SIZE
          }
        });
      }
    }
  }, {
    key: 'render',
    value: function render() {
      var resource = this.props.match.params.resource;

      var resourceSchema = this.props.schema && this.props.schema.spec.paths['/' + resource + '/'].post.requestBody.content['application/json'].schema;
      return resourceSchema && _react2.default.createElement(
        _core.Grid,
        { container: true, spacing: 8, className: 'MainContainer' },
        _react2.default.createElement(
          _core.Grid,
          { item: true, xs: 12 },
          _react2.default.createElement(
            _core.Paper,
            { square: true },
            _react2.default.createElement(
              _core.Typography,
              { variant: 'title', className: 'TableTitle PanelTitle' },
              (0, _findKey2.default)(this.props.resourceList, function (resource) {
                return resource === resource;
              })
            ),
            _react2.default.createElement(
              _core.Button,
              {
                component: function component(props) {
                  return _react2.default.createElement(_reactRouterDom.Link, (0, _extends3.default)({ to: 'new' }, props));
                },
                variant: 'contained',
                color: 'primary',
                className: 'ButtonNew'
              },
              'Create New'
            ),
            this.props.resources ? _react2.default.createElement(
              _react.Fragment,
              null,
              _react2.default.createElement(
                'div',
                { className: 'TableContainer' },
                _react2.default.createElement(
                  _core.Table,
                  { className: 'TableContainer' },
                  _react2.default.createElement(
                    _core.TableHead,
                    null,
                    _react2.default.createElement(
                      _core.TableRow,
                      null,
                      _react2.default.createElement(
                        _core.TableCell,
                        { key: 'edit' },
                        'Edit'
                      ),
                      (0, _values2.default)(resourceSchema.properties).map(function (field) {
                        return _react2.default.createElement(
                          _core.TableCell,
                          { key: field.title },
                          field.description
                        );
                      })
                    )
                  ),
                  _react2.default.createElement(
                    _core.TableBody,
                    null,
                    this.props.resources.map(function (item) {
                      return _react2.default.createElement(
                        _core.TableRow,
                        { key: item.id },
                        _react2.default.createElement(
                          _core.TableCell,
                          null,
                          _react2.default.createElement(
                            _reactRouterDom.Link,
                            { to: '' + _api.REL_PATH + resource + '/' + item.id },
                            _react2.default.createElement(
                              _core.Icon,
                              null,
                              'edit'
                            )
                          )
                        ),
                        (0, _values2.default)(resourceSchema.properties).map(function (field) {
                          return _react2.default.createElement(
                            _core.TableCell,
                            { key: field.title },
                            item[field.title]
                          );
                        })
                      );
                    })
                  ),
                  _react2.default.createElement(
                    _core.TableFooter,
                    null,
                    _react2.default.createElement(_core.TableRow, null)
                  )
                )
              ),
              _react2.default.createElement(_core.TablePagination, {
                colSpan: 3,
                component: 'div',
                className: 'TablePagination',
                count: this.props.totalCount,
                rowsPerPage: this.props.rowsPerPage,
                page: this.props.currentPage - 1,
                onChangePage: this.handleChangePage,
                onChangeRowsPerPage: this.handleChangeRowsPerPage,
                ActionsComponent: _TablePaginationActions2.default,
                rowsPerPageOptions: [0]
              })
            ) : _react2.default.createElement(
              'div',
              { className: 'SpinnerContainer' },
              _react2.default.createElement(_core.CircularProgress, null)
            )
          )
        )
      );
    }
  }]);
  return ListPage;
}(_react2.default.Component);

ListPage.propTypes = propTypes;

var mapStateToProps = function mapStateToProps(state) {
  return {
    rowsPerPage: state.resource.rowsPerPage,
    currentPage: state.resource.currentPage,
    totalCount: state.resource.totalCount,
    resources: state.resource.entities,
    schema: state.metadata.client,
    resourceList: state.metadata.resources
  };
};

var mapDispatchToProps = {
  fetchResources: _resource.fetchResourceEntitiesRequest
};
exports.default = (0, _reactRedux.connect)(mapStateToProps, mapDispatchToProps)(ListPage);

/***/ }),

/***/ "./admin/routes/index.js":
/*!*******************************!*\
  !*** ./admin/routes/index.js ***!
  \*******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _getPrototypeOf = __webpack_require__(/*! babel-runtime/core-js/object/get-prototype-of */ "./node_modules/babel-runtime/core-js/object/get-prototype-of.js");

var _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf);

var _classCallCheck2 = __webpack_require__(/*! babel-runtime/helpers/classCallCheck */ "./node_modules/babel-runtime/helpers/classCallCheck.js");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _createClass2 = __webpack_require__(/*! babel-runtime/helpers/createClass */ "./node_modules/babel-runtime/helpers/createClass.js");

var _createClass3 = _interopRequireDefault(_createClass2);

var _possibleConstructorReturn2 = __webpack_require__(/*! babel-runtime/helpers/possibleConstructorReturn */ "./node_modules/babel-runtime/helpers/possibleConstructorReturn.js");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = __webpack_require__(/*! babel-runtime/helpers/inherits */ "./node_modules/babel-runtime/helpers/inherits.js");

var _inherits3 = _interopRequireDefault(_inherits2);

var _react = __webpack_require__(/*! react */ "./node_modules/react/index.js");

var _react2 = _interopRequireDefault(_react);

var _reactRouterDom = __webpack_require__(/*! react-router-dom */ "./node_modules/react-router-dom/es/index.js");

var _reactRouterRedux = __webpack_require__(/*! react-router-redux */ "./node_modules/react-router-redux/es/index.js");

var _Header = __webpack_require__(/*! ../components/Header */ "./admin/components/Header/index.js");

var _Header2 = _interopRequireDefault(_Header);

var _HomePage = __webpack_require__(/*! ./HomePage */ "./admin/routes/HomePage.js");

var _HomePage2 = _interopRequireDefault(_HomePage);

var _ListPage = __webpack_require__(/*! ./ListPage */ "./admin/routes/ListPage.jsx");

var _ListPage2 = _interopRequireDefault(_ListPage);

var _DetailPage = __webpack_require__(/*! ./DetailPage */ "./admin/routes/DetailPage.jsx");

var _DetailPage2 = _interopRequireDefault(_DetailPage);

var _ErrorPage = __webpack_require__(/*! ./ErrorPage */ "./admin/routes/ErrorPage.jsx");

var _ErrorPage2 = _interopRequireDefault(_ErrorPage);

var _api = __webpack_require__(/*! ../api */ "./admin/api.js");

var _index = __webpack_require__(/*! ../index.js */ "./admin/index.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var Routes = function (_Component) {
  (0, _inherits3.default)(Routes, _Component);

  function Routes() {
    (0, _classCallCheck3.default)(this, Routes);
    return (0, _possibleConstructorReturn3.default)(this, (Routes.__proto__ || (0, _getPrototypeOf2.default)(Routes)).apply(this, arguments));
  }

  (0, _createClass3.default)(Routes, [{
    key: 'render',
    value: function render() {
      return _react2.default.createElement(
        _reactRouterRedux.ConnectedRouter,
        { history: _index.history },
        _react2.default.createElement(
          'div',
          null,
          _react2.default.createElement(_Header2.default, null),
          _react2.default.createElement(
            _reactRouterDom.Switch,
            null,
            _react2.default.createElement(_reactRouterDom.Route, { exact: true, path: _api.REL_PATH, component: _HomePage2.default }),
            _react2.default.createElement(_reactRouterDom.Route, { exact: true, path: _api.REL_PATH + ':resource', component: _ListPage2.default }),
            _react2.default.createElement(_reactRouterDom.Route, {
              exact: true,
              path: _api.REL_PATH + ':resource/:id',
              component: _DetailPage2.default
            }),
            _react2.default.createElement(_reactRouterDom.Route, { path: '/not-found', component: _ErrorPage2.default }),
            _react2.default.createElement(_reactRouterDom.Route, { component: _ErrorPage2.default })
          )
        )
      );
    }
  }]);
  return Routes;
}(_react.Component);

exports.default = Routes;

/***/ }),

/***/ "./admin/sagas/index.js":
/*!******************************!*\
  !*** ./admin/sagas/index.js ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _regenerator = __webpack_require__(/*! babel-runtime/regenerator */ "./node_modules/babel-runtime/regenerator/index.js");

var _regenerator2 = _interopRequireDefault(_regenerator);

exports.default = root;

var _effects = __webpack_require__(/*! redux-saga/effects */ "./node_modules/redux-saga/es/effects.js");

var _metadata = __webpack_require__(/*! ./metadata */ "./admin/sagas/metadata.js");

var _metadata2 = _interopRequireDefault(_metadata);

var _resource = __webpack_require__(/*! ./resource */ "./admin/sagas/resource.js");

var _resource2 = _interopRequireDefault(_resource);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var _marked = /*#__PURE__*/_regenerator2.default.mark(root);

function root() {
  return _regenerator2.default.wrap(function root$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.next = 2;
          return (0, _effects.all)([(0, _metadata2.default)(), (0, _resource2.default)()]);

        case 2:
        case 'end':
          return _context.stop();
      }
    }
  }, _marked, this);
}

/***/ }),

/***/ "./admin/sagas/metadata.js":
/*!*********************************!*\
  !*** ./admin/sagas/metadata.js ***!
  \*********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _regenerator = __webpack_require__(/*! babel-runtime/regenerator */ "./node_modules/babel-runtime/regenerator/index.js");

var _regenerator2 = _interopRequireDefault(_regenerator);

var _extends2 = __webpack_require__(/*! babel-runtime/helpers/extends */ "./node_modules/babel-runtime/helpers/extends.js");

var _extends3 = _interopRequireDefault(_extends2);

exports.default = watchMetadata;

var _effects = __webpack_require__(/*! redux-saga/effects */ "./node_modules/redux-saga/es/effects.js");

var _metadata = __webpack_require__(/*! ../ducks/metadata */ "./admin/ducks/metadata.js");

var _api = __webpack_require__(/*! ../api */ "./admin/api.js");

var _api2 = _interopRequireDefault(_api);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var _marked = /*#__PURE__*/_regenerator2.default.mark(fetchMetadata),
    _marked2 = /*#__PURE__*/_regenerator2.default.mark(watchMetadata);

function fetchMetadata() {
  var metadata, client;
  return _regenerator2.default.wrap(function fetchMetadata$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.prev = 0;
          _context.next = 3;
          return (0, _effects.call)(_api2.default.fetchMetadata);

        case 3:
          metadata = _context.sent;
          _context.next = 6;
          return (0, _effects.call)(_api2.default.fetchSwaggerSchema, metadata.schema);

        case 6:
          client = _context.sent;
          _context.next = 9;
          return (0, _effects.put)((0, _metadata.fetchMetadataSuccess)((0, _extends3.default)({}, metadata, {
            client: client
          })));

        case 9:
          _context.next = 14;
          break;

        case 11:
          _context.prev = 11;
          _context.t0 = _context['catch'](0);
          throw Error(_context.t0);

        case 14:
        case 'end':
          return _context.stop();
      }
    }
  }, _marked, this, [[0, 11]]);
}

function watchMetadata() {
  return _regenerator2.default.wrap(function watchMetadata$(_context2) {
    while (1) {
      switch (_context2.prev = _context2.next) {
        case 0:
          _context2.next = 2;
          return (0, _effects.takeLatest)(_metadata.FETCH_METADATA_REQUEST, fetchMetadata);

        case 2:
        case 'end':
          return _context2.stop();
      }
    }
  }, _marked2, this);
}

/***/ }),

/***/ "./admin/sagas/resource.js":
/*!*********************************!*\
  !*** ./admin/sagas/resource.js ***!
  \*********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _regenerator = __webpack_require__(/*! babel-runtime/regenerator */ "./node_modules/babel-runtime/regenerator/index.js");

var _regenerator2 = _interopRequireDefault(_regenerator);

exports.default = watchResource;

var _effects = __webpack_require__(/*! redux-saga/effects */ "./node_modules/redux-saga/es/effects.js");

var _schema = __webpack_require__(/*! ../selectors/schema */ "./admin/selectors/schema.js");

var _reactRouterRedux = __webpack_require__(/*! react-router-redux */ "./node_modules/react-router-redux/es/index.js");

var _api = __webpack_require__(/*! ../api */ "./admin/api.js");

var _api2 = _interopRequireDefault(_api);

var _resource = __webpack_require__(/*! ../ducks/resource */ "./admin/ducks/resource.js");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var _marked = /*#__PURE__*/_regenerator2.default.mark(fetchResource),
    _marked2 = /*#__PURE__*/_regenerator2.default.mark(submitResource),
    _marked3 = /*#__PURE__*/_regenerator2.default.mark(updateResourceElement),
    _marked4 = /*#__PURE__*/_regenerator2.default.mark(fetchResourceElement),
    _marked5 = /*#__PURE__*/_regenerator2.default.mark(deleteResourceElement),
    _marked6 = /*#__PURE__*/_regenerator2.default.mark(watchResource);

function fetchResource(_ref) {
  var payload = _ref.payload;
  var client, metadata, schema, resources;
  return _regenerator2.default.wrap(function fetchResource$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.prev = 0;
          _context.next = 3;
          return (0, _effects.select)(_schema.selectClient);

        case 3:
          client = _context.sent;

          if (client) {
            _context.next = 12;
            break;
          }

          _context.next = 7;
          return (0, _effects.call)(_api2.default.fetchMetadata);

        case 7:
          metadata = _context.sent;
          schema = metadata.schema;
          _context.next = 11;
          return (0, _effects.call)(_api2.default.fetchSwaggerSchema, schema);

        case 11:
          client = _context.sent;

        case 12:
          _context.next = 14;
          return (0, _effects.call)(_api2.default.fetchResource, payload, client);

        case 14:
          resources = _context.sent;
          _context.next = 17;
          return (0, _effects.put)((0, _resource.fetchResourceEntitiesSuccess)({ resources: resources }));

        case 17:
          _context.next = 23;
          break;

        case 19:
          _context.prev = 19;
          _context.t0 = _context['catch'](0);
          _context.next = 23;
          return (0, _effects.put)((0, _reactRouterRedux.push)('/not-found'));

        case 23:
        case 'end':
          return _context.stop();
      }
    }
  }, _marked, this, [[0, 19]]);
}

function submitResource(_ref2) {
  var payload = _ref2.payload;
  var client, response, errors;
  return _regenerator2.default.wrap(function submitResource$(_context2) {
    while (1) {
      switch (_context2.prev = _context2.next) {
        case 0:
          _context2.prev = 0;
          _context2.next = 3;
          return (0, _effects.select)(_schema.selectClient);

        case 3:
          client = _context2.sent;
          _context2.next = 6;
          return (0, _effects.call)(_api2.default.submitResource, payload, client);

        case 6:
          response = _context2.sent;
          _context2.next = 9;
          return (0, _effects.put)((0, _resource.submitResourceSuccess)(response));

        case 9:
          _context2.next = 11;
          return (0, _effects.put)((0, _reactRouterRedux.push)('' + _api.REL_PATH + payload.resourceName + '/'));

        case 11:
          _context2.next = 18;
          break;

        case 13:
          _context2.prev = 13;
          _context2.t0 = _context2['catch'](0);
          errors = JSON.parse(_context2.t0.message);
          _context2.next = 18;
          return (0, _effects.put)((0, _resource.submitResourceFailure)(errors));

        case 18:
        case 'end':
          return _context2.stop();
      }
    }
  }, _marked2, this, [[0, 13]]);
}

function updateResourceElement(_ref3) {
  var payload = _ref3.payload;
  var client, response;
  return _regenerator2.default.wrap(function updateResourceElement$(_context3) {
    while (1) {
      switch (_context3.prev = _context3.next) {
        case 0:
          _context3.prev = 0;
          _context3.next = 3;
          return (0, _effects.select)(_schema.selectClient);

        case 3:
          client = _context3.sent;
          _context3.next = 6;
          return (0, _effects.call)(_api2.default.updateResourceElement, payload, client);

        case 6:
          response = _context3.sent;
          _context3.next = 9;
          return (0, _effects.put)((0, _resource.updateResourceElementSuccess)(response));

        case 9:
          _context3.next = 11;
          return (0, _effects.put)((0, _reactRouterRedux.push)('' + _api.REL_PATH + payload.resourceName + '/'));

        case 11:
          _context3.next = 15;
          break;

        case 13:
          _context3.prev = 13;
          _context3.t0 = _context3['catch'](0);

        case 15:
        case 'end':
          return _context3.stop();
      }
    }
  }, _marked3, this, [[0, 13]]);
}

function fetchResourceElement(_ref4) {
  var payload = _ref4.payload;
  var client, metadata, schema, resource;
  return _regenerator2.default.wrap(function fetchResourceElement$(_context4) {
    while (1) {
      switch (_context4.prev = _context4.next) {
        case 0:
          _context4.prev = 0;
          _context4.next = 3;
          return (0, _effects.select)(_schema.selectClient);

        case 3:
          client = _context4.sent;

          if (client) {
            _context4.next = 12;
            break;
          }

          _context4.next = 7;
          return (0, _effects.call)(_api2.default.fetchMetadata);

        case 7:
          metadata = _context4.sent;
          schema = metadata.schema;
          _context4.next = 11;
          return (0, _effects.call)(_api2.default.fetchSwaggerSchema, schema);

        case 11:
          client = _context4.sent;

        case 12:
          _context4.next = 14;
          return (0, _effects.call)(_api2.default.fetchResourceElement, payload, client);

        case 14:
          resource = _context4.sent;
          _context4.next = 17;
          return (0, _effects.put)((0, _resource.fetchCurrentResourceSuccess)(resource));

        case 17:
          _context4.next = 23;
          break;

        case 19:
          _context4.prev = 19;
          _context4.t0 = _context4['catch'](0);
          _context4.next = 23;
          return (0, _effects.put)((0, _reactRouterRedux.push)('/not-found'));

        case 23:
        case 'end':
          return _context4.stop();
      }
    }
  }, _marked4, this, [[0, 19]]);
}

function deleteResourceElement(_ref5) {
  var payload = _ref5.payload;
  var client, metadata, schema;
  return _regenerator2.default.wrap(function deleteResourceElement$(_context5) {
    while (1) {
      switch (_context5.prev = _context5.next) {
        case 0:
          _context5.prev = 0;
          _context5.next = 3;
          return (0, _effects.select)(_schema.selectClient);

        case 3:
          client = _context5.sent;

          if (client) {
            _context5.next = 12;
            break;
          }

          _context5.next = 7;
          return (0, _effects.call)(_api2.default.fetchMetadata);

        case 7:
          metadata = _context5.sent;
          schema = metadata.schema;
          _context5.next = 11;
          return (0, _effects.call)(_api2.default.fetchSwaggerSchema, schema);

        case 11:
          client = _context5.sent;

        case 12:
          _context5.next = 14;
          return (0, _effects.call)(_api2.default.deleteResourceElement, payload, client);

        case 14:
          _context5.next = 16;
          return (0, _effects.put)((0, _reactRouterRedux.push)('' + _api.REL_PATH + payload.resourceName + '/'));

        case 16:
          _context5.next = 20;
          break;

        case 18:
          _context5.prev = 18;
          _context5.t0 = _context5['catch'](0);

        case 20:
        case 'end':
          return _context5.stop();
      }
    }
  }, _marked5, this, [[0, 18]]);
}

function watchResource() {
  return _regenerator2.default.wrap(function watchResource$(_context6) {
    while (1) {
      switch (_context6.prev = _context6.next) {
        case 0:
          _context6.next = 2;
          return (0, _effects.takeLatest)(_resource.FETCH_RESOURCE_ENTITIES_REQUEST, fetchResource);

        case 2:
          _context6.next = 4;
          return (0, _effects.takeLatest)(_resource.SUBMIT_RESOURCE_REQUEST, submitResource);

        case 4:
          _context6.next = 6;
          return (0, _effects.takeLatest)(_resource.FETCH_CURRENT_RESOURCE_REQUEST, fetchResourceElement);

        case 6:
          _context6.next = 8;
          return (0, _effects.takeLatest)(_resource.UPDATE_RESOURCE_ELEMENT_REQUEST, updateResourceElement);

        case 8:
          _context6.next = 10;
          return (0, _effects.takeLatest)(_resource.DELETE_RESOURCE_ELEMENT_REQUEST, deleteResourceElement);

        case 10:
        case 'end':
          return _context6.stop();
      }
    }
  }, _marked6, this);
}

/***/ }),

/***/ "./admin/selectors/schema.js":
/*!***********************************!*\
  !*** ./admin/selectors/schema.js ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});
var selectSchemaUrl = exports.selectSchemaUrl = function selectSchemaUrl(state) {
  return state.metadata.schema;
};
var selectClient = exports.selectClient = function selectClient(state) {
  return state.metadata.client;
};

/***/ })

},[["./admin/index.js","runtime~index","styles.react","vendors~index"]]]);
//# sourceMappingURL=index.js.map