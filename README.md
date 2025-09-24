in this github repo please find the selenium code in the file **testing.py**

In order to run this please install **pip** and **python**

Then create a virtual environment by `python -m venv YOUR_ENV_NAME`

Once created activate it by running the ps1.exe in bin

then run `pip install selenium`

To Run the laravel server make sure you have **php** and **mysql** installed

Note i have changed the actual test domain name to local host **https://127.0.0.1:8000/**
Same changes have been made in app routing

To start the server run `php artisan serve`
And to run the automation selenium file in a new terminal after going to parent dir run `python testing.py`

Task -3
The html page named app-calendar.html has been placed as **app-calendar.blade.php**

`Route::get('calendar',[App\Http\Controllers\Caller\LoginController::class,'go_to_calendar']); //Route added as task - 3`
This code has been added in web.php in routes

The corresponding controller code has been added in the same **LoginController.php**

Refferencing code in **LoginController.php** is
`public function go_to_calendar(Request $request){
                        return View("caller.calendar.app-calendar");
                }`
To see the calendar page first run the server using specefied command while being in `Root\main-laravel\`

And in the url add a calendar field.
**http://127.0.0.1:8000/calendar**

All three specefied tasks are done
Check github log or history to see all the respective code changes.
