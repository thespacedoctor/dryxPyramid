# dryxPyramid

`dryxPyramid` is a python package containing some basic, reusable code for Pyramid Webapps. It contains:

## Renderers

`dryxPyramid` contains some new and overriding renderers that allow for the download of files using `filename=myfilename` in the query string.

* csv (`format=csv`)
* json (`format=json`)
* plain text tables (`format=plain_table`)
* plain text (`format=plain_text`)

## API

| **Resource**  | **Post** | **Get** | **Put** | **Delete** | 
| :------------ | :----------- | :----------- | :----------- | :----------- |
| **/download**     | Not Allowed  | Download requested data  | Not Allowed  | Not Allowed  | 

### Reserved Query String Parameters

| Parameter Key | Description | Some Common Values |
| :------ | :------- | :------- |
| format | The format to display the data in | json, csv, plain_table, plain_text |
| filename | Download the data in the specified `format` with this filename | |


## View Permissions 

There are currently 6 levels of tiered view-permissions that can be added to the view decorators. Each level of permissions includes the acummulated permissions up to that tier.

1. `view_everyone`: viewable by the public
2. `view_users`: viewable by logged in users
3. `edit_users`: viewable by users with the `edit_users` permissions
4. `superuser`: viewable by users with `superuser` permissions
5. `admin`: viewable by users with `admin` permissions
6. `superadmin`: viewable by users with `superadmin` permissions
