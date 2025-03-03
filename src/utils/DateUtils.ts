export class DateUtils {
  public static formatUnixToDate(unixTime: number): string {
    const date = new Date(unixTime * 1000); // Умножаем на 1000, если время в секундах

    const months = [
      "Jan", "Feb", "Mar", "Apr", "May", "Jun",
      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ];

    const day = date.getDate();
    const month = months[date.getMonth()];
    const year = date.getFullYear();

    return `${day} ${month} ${year}`;
  }
}