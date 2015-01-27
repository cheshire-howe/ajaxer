module.exports = function(grunt) {
    grunt.initConfig({
        less: {
            development: {
                options: {
                    paths: ["src/less"]
                },
                files: {"static/css/custom.css": "src/less/main.less"}
            }
        }
    });
};
